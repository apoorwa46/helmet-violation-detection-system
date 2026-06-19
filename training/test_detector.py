import sys
from pathlib import Path

# Add the project root so this standalone script can import app.services.
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import cv2

from app.services.detector import HelmetDetector

# Initialize the production detector with the trained application model.
detector = HelmetDetector()

# Load one known test image as a quick inference smoke test.
image = cv2.imread(
    "datasets/processed/test/images/BikesHelmets1.png"
)

# Run detection and print the raw Ultralytics result for manual inspection.
results = detector.detect(image)

print(results)
