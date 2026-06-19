import sys
from pathlib import Path

# Locate the repository root so app.services imports work in a direct run.
ROOT_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

# Add the root to Python's module search path for this test script.
sys.path.append(
    str(ROOT_DIR)
)

from app.services.video_processor import (
    VideoProcessor
)

# The full processor includes violation sampling and evidence-image creation.
processor = VideoProcessor()

# Run the sample video to manually verify generated violation records/images.
processor.process_video(
    "uploads/test_video.mp4"
)
