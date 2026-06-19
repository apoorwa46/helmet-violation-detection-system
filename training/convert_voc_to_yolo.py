import xml.etree.ElementTree as ET
from pathlib import Path
import shutil

# ==========================================================
# Class Mapping
# ==========================================================

# YOLO label files use zero-based numeric class IDs rather than class names.
CLASS_MAP = {
    "With Helmet": 0,
    "Without Helmet": 1
}

# ==========================================================
# Paths
# ==========================================================

# Source folders contain the original images and Pascal VOC XML annotations.
RAW_IMAGES_DIR = Path("datasets/raw/images")
RAW_ANNOTATIONS_DIR = Path("datasets/raw/annotations")

PROCESSED_DIR = Path("datasets/processed")

# Converted files are staged together before the train/valid/test split.
ALL_IMAGES_DIR = PROCESSED_DIR / "all_images"
ALL_LABELS_DIR = PROCESSED_DIR / "all_labels"

# Create destination folders if this is the first conversion run.
ALL_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
ALL_LABELS_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Bounding Box Conversion
# ==========================================================


def convert_bbox(img_width, img_height, xmin, ymin, xmax, ymax):
    # Pascal VOC stores absolute corner coordinates. YOLO expects normalized
    # center coordinates and box dimensions, each in the range 0 to 1.
    x_center = ((xmin + xmax) / 2) / img_width
    y_center = ((ymin + ymax) / 2) / img_height

    width = (xmax - xmin) / img_width
    height = (ymax - ymin) / img_height

    # Limiting precision keeps label files compact without meaningful loss.
    return (
        round(x_center, 6),
        round(y_center, 6),
        round(width, 6),
        round(height, 6)
    )


# ==========================================================
# Convert Pascal VOC XML → YOLO TXT
# ==========================================================

# Process every XML annotation available in the raw annotation directory.
xml_files = list(RAW_ANNOTATIONS_DIR.glob("*.xml"))

print(f"Found {len(xml_files)} annotation files")

for xml_file in xml_files:

    # Parse the XML tree and read the image dimensions used for normalization.
    tree = ET.parse(xml_file)
    root = tree.getroot()

    size = root.find("size")

    img_width = int(size.find("width").text)
    img_height = int(size.find("height").text)

    # Each accepted object becomes one line in the matching YOLO text file.
    yolo_lines = []

    for obj in root.findall("object"):

        class_name = obj.find("name").text.strip()

        # Ignore annotation classes that this two-class model does not train on.
        if class_name not in CLASS_MAP:
            continue

        class_id = CLASS_MAP[class_name]

        # Read the object's absolute Pascal VOC bounding-box corners.
        bbox = obj.find("bndbox")

        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)

        # Convert corners into YOLO's normalized center/size representation.
        x, y, w, h = convert_bbox(
            img_width,
            img_height,
            xmin,
            ymin,
            xmax,
            ymax
        )

        yolo_lines.append(
            f"{class_id} {x} {y} {w} {h}"
        )

    # Save one YOLO label file with the same stem as the source annotation.
    label_path = ALL_LABELS_DIR / f"{xml_file.stem}.txt"

    with open(label_path, "w") as f:
        f.write("\n".join(yolo_lines))

    # Copy the matching image while supporting common image extensions.
    image_extensions = [".jpg", ".jpeg", ".png"]

    for ext in image_extensions:
        image_path = RAW_IMAGES_DIR / f"{xml_file.stem}{ext}"

        if image_path.exists():
            # copy2 preserves source file metadata where the platform permits.
            shutil.copy2(
                image_path,
                ALL_IMAGES_DIR / image_path.name
            )
            break

print("\nVOC → YOLO conversion complete.")
print(f"Images copied to: {ALL_IMAGES_DIR}")
print(f"Labels saved to: {ALL_LABELS_DIR}")
