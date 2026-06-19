import sys
from pathlib import Path

# Resolve the repository root from this script's location rather than relying
# on the terminal's current import path.
ROOT_DIR = Path(
    __file__
).resolve().parent.parent

# Make the app package importable when this file is executed directly.
sys.path.append(
    str(ROOT_DIR)
)

from app.services.video_processor import (
    VideoProcessor
)

# Build the same processing pipeline used by the application.
processor = VideoProcessor()

# Process the sample upload and create video, violation, and report outputs.
processor.process_video(
    "uploads/test_video.mp4"
)
