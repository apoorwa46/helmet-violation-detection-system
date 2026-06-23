from pathlib import Path

import cv2


class ViolationService:

    def __init__(self):

        self.output_dir = Path(
            "outputs/violations"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.violations = []

    def save_violation(
        self,
        frame,
        frame_number,
        timestamp,
        confidence
    ):

        filename = (
            f"violation_{frame_number}.jpg"
        )

        filepath = (
            self.output_dir / filename
        )

        cv2.imwrite(
            str(filepath),
            frame
        )

        violation = {

            "frame": frame_number,
            "timestamp": timestamp,
            "confidence": confidence,
            "image": filename
        }

        self.violations.append(
            violation
        )

        return violation

    def get_violations(self):

        return self.violations