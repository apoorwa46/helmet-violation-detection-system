import cv2
import random

from pathlib import Path

# Use training images and their corresponding YOLO labels for spot checking.
IMAGE_DIR = Path(
    "datasets/processed/train/images"
)

LABEL_DIR = Path(
    "datasets/processed/train/labels"
)

# Random ordering helps inspect a different sample across manual runs.
images = list(
    IMAGE_DIR.glob("*")
)

random.shuffle(images)

for image_path in images[:20]:

    # Load the image and capture its pixel dimensions for coordinate conversion.
    image = cv2.imread(
        str(image_path)
    )

    h, w, _ = image.shape

    # YOLO label files have the same filename stem as their images.
    label_path = (
        LABEL_DIR /
        f"{image_path.stem}.txt"
    )

    with open(label_path) as f:

        for line in f:

            # YOLO rows contain class ID, normalized center, width, and height.
            cls, xc, yc, bw, bh = map(
                float,
                line.split()
            )

            # Convert normalized center/size values back to pixel corners.
            xmin = int(
                (xc - bw/2) * w
            )

            ymin = int(
                (yc - bh/2) * h
            )

            xmax = int(
                (xc + bw/2) * w
            )

            ymax = int(
                (yc + bh/2) * h
            )

            # Draw the ground-truth box in green for visual validation.
            cv2.rectangle(
                image,
                (xmin, ymin),
                (xmax, ymax),
                (0,255,0),
                2
            )

    cv2.imshow(
        "Label Check",
        image
    )

    # Pause on each sample; pressing Escape exits before all 20 are shown.
    key = cv2.waitKey(0)

    if key == 27:
        break

# Close any OpenCV display windows after completion or early exit.
cv2.destroyAllWindows()
