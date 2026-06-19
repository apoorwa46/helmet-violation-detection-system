from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"

OUTPUT_VIDEO_DIR = BASE_DIR / "outputs/videos"

VIOLATION_DIR = BASE_DIR / "outputs/violations"

REPORT_DIR = BASE_DIR / "outputs/reports"