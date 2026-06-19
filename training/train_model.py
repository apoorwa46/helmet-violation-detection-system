from ultralytics import YOLO

# ==================================================

# Load Base YOLO Model

# ==================================================

# Start from lightweight pretrained YOLOv8 Nano weights. Transfer learning
# reduces the data and time needed for the custom helmet classes.
model = YOLO("yolov8n.pt")

# ==================================================

# Train

# ==================================================

# Train using paths/classes from data.yaml. Ultralytics saves checkpoints and
# metrics beneath the configured project/name directory.
results = model.train(
# Dataset definition containing split locations and class names.
data="datasets/processed/data.yaml",
# Maximum number of full passes through the training dataset.
epochs=50,
# Resize training images to 640 pixels for the model input.
imgsz=640,
# Number of images processed together in each optimization step.
batch=16,
# Parent directory for generated training artifacts.
project="runs",
# Human-readable subdirectory name for this experiment.
name="helmet_training",
# Stop early after 10 epochs without validation improvement.
patience=10,
# Preserve checkpoints so the best trained weights can be reused.
save=True
)

print("Training Complete")
