from pathlib import Path

# Check every prepared dataset split for images that have no matching label.
SPLITS = ["train", "valid", "test"]

for split in SPLITS:

    # YOLO keeps images and labels in sibling directories for each split.
    image_dir = Path(
        f"datasets/processed/{split}/images"
    )

    label_dir = Path(
        f"datasets/processed/{split}/labels"
    )

    # Gather all image files regardless of their extension.
    images = list(image_dir.glob("*"))

    # Store missing filenames so a few examples can be shown after counting.
    missing_labels = []

    for image in images:

        # Labels must share the image stem, with a .txt extension.
        label_file = (
            label_dir /
            f"{image.stem}.txt"
        )

        if not label_file.exists():
            missing_labels.append(
                image.name
            )

    # Print a compact verification summary for the current split.
    print("\n" + "="*30)
    print(split.upper())

    print(
        f"Images: {len(images)}"
    )

    print(
        f"Missing Labels: {len(missing_labels)}"
    )

    if missing_labels:
        # Limit example output so a large broken dataset stays readable.
        print(missing_labels[:5])
