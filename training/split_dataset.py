from pathlib import Path
import shutil
import random

# ==================================================
# Paths
# ==================================================

DATASET_DIR = Path("datasets/processed")

# Conversion places all paired files here before this script divides them.
IMAGES_DIR = DATASET_DIR / "all_images"
LABELS_DIR = DATASET_DIR / "all_labels"

# ==================================================
# Output Folders
# ==================================================

SPLITS = ["train", "valid", "test"]

for split in SPLITS:
    # YOLO expects separate images/labels folders inside every split.
    (DATASET_DIR / split / "images").mkdir(
        parents=True,
        exist_ok=True
    )

    (DATASET_DIR / split / "labels").mkdir(
        parents=True,
        exist_ok=True
    )

# ==================================================
# Collect Images
# ==================================================

# Gather source images, then use a fixed seed for a reproducible split.
images = list(IMAGES_DIR.glob("*"))

random.seed(42)
random.shuffle(images)

# ==================================================
# Split Ratios
# ==================================================

# Allocate 70% training, 20% validation, and the remainder to testing.
total = len(images)

train_count = int(total * 0.7)
valid_count = int(total * 0.2)

train_images = images[:train_count]

valid_images = images[
    train_count:train_count + valid_count
]

test_images = images[
    train_count + valid_count:
]

# ==================================================
# Copy Function
# ==================================================

def copy_files(image_list, split_name):

    # Copy each image and its same-stem YOLO label into the selected split.
    for image_path in image_list:

        # Example: image001.jpg is paired with image001.txt.
        label_path = (
            LABELS_DIR /
            f"{image_path.stem}.txt"
        )

        shutil.copy2(
            image_path,
            DATASET_DIR /
            split_name /
            "images" /
            image_path.name
        )

        shutil.copy2(
            label_path,
            DATASET_DIR /
            split_name /
            "labels" /
            label_path.name
        )

# ==================================================
# Execute Split
# ==================================================

# Materialize all three split lists on disk.
copy_files(train_images, "train")
copy_files(valid_images, "valid")
copy_files(test_images, "test")

print("Dataset split complete!")

print(f"Train: {len(train_images)}")
print(f"Valid: {len(valid_images)}")
print(f"Test : {len(test_images)}")
