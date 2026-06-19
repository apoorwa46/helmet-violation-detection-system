from ultralytics import YOLO

# Thin wrapper around Ultralytics so the rest of the application does not
# need to know where the model is stored or how inference is invoked.
class HelmetDetector:
    def __init__(self):
        # Load the trained weights once when the service is created. Reusing
        # this object avoids loading the model again for every video frame.
        self.model = YOLO("models/helmet_detector_v1.pt")  # Load the trained YOLO model
    
    def detect(self,frame):
        # Disable verbose output because this method is called once per frame.
        # The returned Ultralytics result still contains boxes, classes,
        # confidence scores, and coordinates needed by downstream services.
        results = self.model(frame, verbose=False)  # Perform detection on the input frame
        return results
    
