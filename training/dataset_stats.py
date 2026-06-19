from pathlib import Path

# Aggregate labels from every dataset split to inspect overall class balance.
LABEL_DIRS = [

    Path(
        "datasets/processed/train/labels"
    ),

    Path(
        "datasets/processed/valid/labels"
    ),

    Path(
        "datasets/processed/test/labels"
    )
]

# Class IDs follow data.yaml: 0 is helmet and 1 is no helmet.
helmet_count = 0
no_helmet_count = 0

for label_dir in LABEL_DIRS:

    # Every image has a corresponding text file containing zero or more boxes.
    for txt_file in label_dir.glob("*.txt"):

        with open(txt_file) as f:

            for line in f:

                # The first whitespace-separated value on a YOLO row is class.
                class_id = int(
                    line.split()[0]
                )

                if class_id == 0:
                    helmet_count += 1

                elif class_id == 1:
                    no_helmet_count += 1

# Print totals after all train, validation, and test labels are counted.
print("\nDataset Statistics")

print(
    f"Helmet: {helmet_count}"
)

print(
    f"No Helmet: {no_helmet_count}"
)

print(
    f"Total Objects: {helmet_count + no_helmet_count}"
)
