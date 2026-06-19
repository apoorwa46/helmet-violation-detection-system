from ultralytics import YOLO

# Load the best checkpoint selected during training rather than the last epoch.
model = YOLO(
"runs/detect/runs/helmet_training/weights/best.pt"
)

# Evaluate against the validation configuration stored with the trained model.
metrics = model.val()

# Print Ultralytics' precision, recall, and mAP-related validation results.
print(metrics)
