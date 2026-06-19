import cv2


class DetectionVisualizer:

    def draw_boxes(
        self,
        frame,
        results
    ):

        # Ultralytics returns a list of results; this application performs
        # inference on one frame at a time, so its detections are at index 0.
        for box in results[0].boxes:

            # Convert tensor values to regular Python numbers for comparisons
            # and formatting.
            class_id = int(
                box.cls[0]
            )

            confidence = float(
                box.conf[0]
            )

            # xyxy stores the top-left and bottom-right box pixel coordinates.
            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            # Green communicates compliance; red highlights a violation.
            if class_id == 0:

                label = "With Helmet"

                color = (0, 255, 0)

            else:

                label = "Without Helmet"

                color = (0, 0, 255)

            # Draw the detection boundary around the rider/person.
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                2
            )

            # Place the class label and confidence immediately above the box.
            cv2.putText(
                frame,
                f"{label} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2
            )

        # OpenCV edits the frame in place; returning it keeps the pipeline clear.
        return frame
