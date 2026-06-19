from ultralytics import YOLO

# Load the best checkpoint produced by the helmet-training run.
model = YOLO(
    'runs/detect/runs/helmet_training/weights/best.pt'
)

# Predict every image in the test folder. save=True writes annotated copies
# into Ultralytics' standard runs directory for visual review.
results = model.predict(
    source="datasets/processed/test/images",
    save=True,
    conf=0.5
)
