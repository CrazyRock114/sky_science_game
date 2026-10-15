#!/usr/bin/env python3
"""
Automated Batch Renderer for IGCSE Science Knowledge Animations
Renders all 6 animation HTML files to 1080P 30fps MP4 with British English audio.
"""

import sys
import time
import base64
import http.server
import socketserver
import subprocess
import threading
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent.resolve()
VIDEOS_DIR = ROOT / 'videos'
STILLS_DIR = ROOT / 'stills'
VIDEOS_DIR.mkdir(exist_ok=True)
STILLS_DIR.mkdir(exist_ok=True)

ANIMATIONS = [
    {
        'id': 't1_dir_a',
        'file': 't1_dir_a.html',
        'topic': 'Topic 1: Mechanics of Breathing',
        'direction': 'Direction A: Kurzgesagt Flat Glowing',
        'audio': ROOT / 'audio' / 't1_ventilation_ryan.wav',
        'duration': 29.18,
        'stills_times': [3.5, 11.0, 16.5, 24.0]
    },
    {
        'id': 't1_dir_b',
        'file': 't1_dir_b.html',
        'topic': 'Topic 1: Mechanics of Breathing',
        'direction': 'Direction B: 3Blue1Brown Geometric Logic',
        'audio': ROOT / 'audio' / 't1_ventilation_ryan.wav',
        'duration': 29.18,
        'stills_times': [3.5, 11.0, 16.5, 24.0]
    },
    {
        'id': 't1_dir_c',
        'file': 't1_dir_c.html',
        'topic': 'Topic 1: Mechanics of Breathing',
        'direction': 'Direction C: Whiteboard & Cambridge Notebook',
        'audio': ROOT / 'audio' / 't1_ventilation_ryan.wav',
        'duration': 29.18,
        'stills_times': [3.5, 11.0, 16.5, 24.0]
    },
    {
        'id': 't2_dir_a',
        'file': 't2_dir_a.html',
        'topic': 'Topic 2: Cardiac Cycle & Valves',
        'direction': 'Direction A: Kurzgesagt Flat Glowing',
        'audio': ROOT / 'audio' / 't2_cardiac_ryan.wav',
        'duration': 28.78,
        'stills_times': [3.5, 11.5, 19.0, 25.5]
    },
    {
        'id': 't2_dir_b',
        'file': 't2_dir_b.html',
        'topic': 'Topic 2: Cardiac Cycle & Valves',
        'direction': 'Direction B: 3Blue1Brown Geometric Logic',
        'audio': ROOT / 'audio' / 't2_cardiac_ryan.wav',
        'duration': 28.78,
        'stills_times': [3.5, 11.5, 19.0, 25.5]
    },
    {
        'id': 't2_dir_c',
        'file': 't2_dir_c.html',
        'topic': 'Topic 2: Cardiac Cycle & Valves',
        'direction': 'Direction C: Whiteboard & Cambridge Notebook',
        'audio': ROOT / 'audio' / 't2_cardiac_ryan.wav',
        'duration': 28.78,
        'stills_times': [3.5, 11.5, 19.0, 25.5]
    }
]

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

def render_item(anim, page, port, fps=30):
    anim_id = anim['id']
    html_file = anim['file']
    audio_file = anim['audio']
    duration = anim['duration']
    out_video = VIDEOS_DIR / f"{anim_id}.mp4"

    print(f"\n=======================================================")
    print(f"🎬 Rendering: {anim['topic']} · {anim['direction']}")
    print(f"   Target: {out_video.name} ({duration}s @ {fps}fps)")
    print(f"=======================================================")

    url = f"http://127.0.0.1:{port}/{html_file}?render=1"
    page.goto(url)
    page.wait_for_function("window.__ready === true", timeout=60000)

    # Export keyframe stills first
    for st in anim['stills_times']:
        still_path = STILLS_DIR / f"{anim_id}_still_{st:.1f}s.png"
        b64 = page.evaluate("""(t) => {
            window.renderFrame(t);
            return window.__canvas.toDataURL('image/png').split(',')[1];
        }""", st)
        still_path.write_bytes(base64.b64decode(b64))
        print(f"   📸 Saved still: {still_path.name}")

    # Launch FFmpeg process with pipe input and audio muxing
    total_frames = int(round(duration * fps))
    cmd = [
        'ffmpeg', '-y', '-v', 'error',
        '-f', 'image2pipe',
        '-framerate', str(fps),
        '-c:v', 'png',
        '-i', '-',
        '-i', str(audio_file),
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-crf', '18',
        '-pix_fmt', 'yuv420p',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-shortest',
        str(out_video)
    ]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    t_start = time.time()
    for frame_idx in range(total_frames):
        t_sec = frame_idx / fps
        b64 = page.evaluate("""(t) => {
            window.renderFrame(t);
            return window.__canvas.toDataURL('image/png').split(',')[1];
        }""", t_sec)
        frame_bytes = base64.b64decode(b64)
        ff.stdin.write(frame_bytes)

        if (frame_idx + 1) % 60 == 0 or frame_idx == total_frames - 1:
            elapsed = time.time() - t_start
            cur_fps = (frame_idx + 1) / max(0.001, elapsed)
            percent = (frame_idx + 1) / total_frames * 100
            print(f"   Frame {frame_idx + 1}/{total_frames} ({percent:.1f}%) · {cur_fps:.1f} fps · {elapsed:.1f}s", flush=True)

    ff.stdin.close()
    ff.wait()

    file_size_mb = out_video.stat().st_size / (1024 * 1024)
    print(f"✅ Finished {out_video.name}: {file_size_mb:.2f} MB ({time.time() - t_start:.1f}s total)")

def main():
    target_id = sys.argv[1] if len(sys.argv) > 1 else None

    # Start local HTTP server
    srv = socketserver.ThreadingTCPServer(('127.0.0.1', 0), QuietHandler)
    srv.daemon_threads = True
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    print(f"Local server started on port {port}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1)

        force = '--force' in sys.argv
        target_id_clean = None if (not target_id or target_id.startswith('--')) else target_id
        targets = [anim for anim in ANIMATIONS if not target_id_clean or anim['id'] == target_id_clean]
        if not targets:
            print(f"Error: Animation ID '{target_id}' not found.")
            sys.exit(1)

        overall_start = time.time()
        for anim in targets:
            out_vid = VIDEOS_DIR / f"{anim['id']}.mp4"
            if out_vid.exists() and out_vid.stat().st_size > 500000 and not force:
                print(f"⏩ Skipping {out_vid.name} (already rendered, {out_vid.stat().st_size / (1024*1024):.2f} MB). Use --force to re-render.")
                continue
            render_item(anim, page, port)

        browser.close()
    srv.shutdown()
    print(f"\n🎉 All {len(targets)} animations successfully rendered in {time.time() - overall_start:.1f}s!")

if __name__ == '__main__':
    main()
