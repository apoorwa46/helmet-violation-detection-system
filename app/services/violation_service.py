from pathlib import Path

import cv2


class ViolationService:

    def __init__(self):

        # Evidence frames are stored separately from processed videos/reports.
        self.output_dir = Path(
            "outputs/violations"
        )

        # Ensure saving can begin immediately, including on the first run.
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        # Hold metadata in memory so VideoProcessor can return a final summary.
        self.violations = []

    def save_violation(
        self,
        frame,
        frame_number,
        timestamp,
        confidence
    ):

        # Include the source frame number to make each evidence name traceable.
        filename = (
            f"violation_{frame_number}.jpg"
        )

        filepath = (
            self.output_dir / filename
        )

        # Save the supplied frame as a JPEG evidence image.
        cv2.imwrite(
            str(filepath),
            frame
        )

        # Record where and when the violation occurred, plus model confidence.
        self.violations.append(
            {
                "frame": frame_number,
                "timestamp": timestamp,
                "confidence": confidence,
                "image": filename
            }
        )

    def get_violations(self):

        # Expose the collected metadata to the video-processing coordinator.
        return self.violations
