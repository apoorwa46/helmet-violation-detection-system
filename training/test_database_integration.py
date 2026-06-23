import sys

from pathlib import Path

ROOT_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.append(
    str(ROOT_DIR)
)

from app.services.video_processor import (
    VideoProcessor
)

processor = VideoProcessor()

processor.process_video(
    "uploads/test_video.mp4"
)