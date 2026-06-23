# import cv2

# from pathlib import Path

# from app.services.detector import (
#     HelmetDetector
# )

# from app.services.visualizer import (
#     DetectionVisualizer
# )

# from app.services.violation_service import (
#     ViolationService
# )

# from app.services.analytics_service import (
#     AnalyticsService
# )

# from app.services.report_service import (
#     ReportService
# )


# class VideoProcessor:

#     def __init__(self):

#         # Compose the full processing pipeline once. Each service has one
#         # responsibility: inference, drawing, violations, analytics, or output.
#         self.detector = HelmetDetector()

#         self.visualizer = (
#             DetectionVisualizer()
#         )

#         self.violation_service = (
#             ViolationService()
#         )

#         self.analytics_service = (
#             AnalyticsService()
#         )

#         self.report_service = (
#             ReportService()
#         )

#     def process_video(
#         self,
#         video_path
#     ):

#         # Open the input video. OpenCV supplies one frame at a time below.
#         cap = cv2.VideoCapture(
#             str(video_path)
#         )

#         # Read source properties so the processed video keeps the same timing
#         # and dimensions as the original file.
#         fps = cap.get(
#             cv2.CAP_PROP_FPS
#         )

#         width = int(
#             cap.get(
#                 cv2.CAP_PROP_FRAME_WIDTH
#             )
#         )

#         height = int(
#             cap.get(
#                 cv2.CAP_PROP_FRAME_HEIGHT
#             )
#         )

#         # All annotated frames are written to this fixed output location.
#         output_path = (
#             Path(
#                 "outputs/processed_videos"
#             )
#             /
#             "processed_video.mp4"
#         )

#         # Configure an MP4 writer using the source video's FPS and resolution.
#         writer = cv2.VideoWriter(
#             str(output_path),
#             cv2.VideoWriter_fourcc(
#                 *"mp4v"
#             ),
#             fps,
#             (width, height)
#         )

#         # Frame numbers are used for progress output and violation timestamps.
#         frame_count = 0

#         while True:

#             # read() returns success=False after the final frame or on failure.
#             success, frame = cap.read()

#             if not success:
#                 break

#             frame_count += 1

#             # Run helmet detection on the current unmodified frame.
#             results = self.detector.detect(
#                 frame
#             )

#             # Inspect every detected person/object to update analytics and
#             # optionally preserve evidence of a no-helmet violation.
#             for box in results[0].boxes:

#                 class_id = int(
#                     box.cls[0]
#                 )

#                 confidence = float(
#                     box.conf[0]
#                 )

#                 # =====================================
#                 # Analytics Tracking
#                 # =====================================

#                 self.analytics_service.add_detection(
#                     class_id
#                 )

#                 # =====================================
#                 # Violation Detection
#                 # =====================================

#                 if class_id == 1:

#                     # Save at most one sample every 30 frames. This reduces
#                     # near-identical violation images from adjacent frames.
#                     if frame_count % 30 == 0:

#                         # Convert the frame position into seconds in the video.
#                         timestamp = (
#                             frame_count / fps
#                         )

#                         self.violation_service.save_violation(
#                             frame=frame,
#                             frame_number=frame_count,
#                             timestamp=round(
#                                 timestamp,
#                                 2
#                             ),
#                             confidence=round(
#                                 confidence,
#                                 2
#                             )
#                         )

#             # Draw labels and bounding boxes only after saving any evidence;
#             # violation images therefore contain the original video frame.
#             frame = (
#                 self.visualizer.draw_boxes(
#                     frame,
#                     results
#                 )
#             )

#             # Add the annotated frame to the processed output video.
#             writer.write(frame)

#             print(
#                 f"Frame {frame_count}"
#             )

#         # Explicitly release native OpenCV resources and finalize the MP4 file.
#         cap.release()

#         writer.release()

#         print(
#             f"\nSaved: {output_path}"
#         )

#         # =====================================
#         # Violations Summary
#         # =====================================

#         # Retrieve all violation metadata collected during this processing run.
#         violations = (
#             self.violation_service
#             .get_violations()
#         )

#         print(
#             f"\nViolations Found: "
#             f"{len(violations)}"
#         )

#         # =====================================
#         # Analytics Report
#         # =====================================

#         # Convert accumulated detection counts into report-ready metrics.
#         analytics = (
#             self.analytics_service
#             .generate_report()
#         )

#         print(
#             "\n========== Analytics Report =========="
#         )

#         for key, value in analytics.items():

#             print(
#                 f"{key}: {value}"
#             )

#         # =====================================
#         # Save Analytics Report
#         # =====================================

#         # Persist the analytics summary separately from the processed video.
#         report_path = (
#             self.report_service
#             .save_report(
#                 analytics
#             )
#         )

#         print(
#             f"\nReport Saved: {report_path}"
#         )

#         # Return every useful artifact to a route, script, or future caller.
#         return {
#             "analytics": analytics,
#             "violations": violations,
#             "report_path": str(report_path),
#             "processed_video": str(output_path)
#         }


import cv2

from pathlib import Path

from app.services.detector import (
    HelmetDetector
)

from app.services.visualizer import (
    DetectionVisualizer
)

from app.services.violation_service import (
    ViolationService
)

from app.services.analytics_service import (
    AnalyticsService
)

from app.services.report_service import (
    ReportService
)

from app.services.database_service import (
    DatabaseService
)


class VideoProcessor:

    def __init__(self):

        # =====================================
        # Core Services
        # =====================================

        self.detector = HelmetDetector()

        self.visualizer = (
            DetectionVisualizer()
        )

        self.violation_service = (
            ViolationService()
        )

        self.analytics_service = (
            AnalyticsService()
        )

        self.report_service = (
            ReportService()
        )

        self.database_service = (
            DatabaseService()
        )

    def process_video(
        self,
        video_path
    ):

        # =====================================
        # Open Video
        # =====================================

        cap = cv2.VideoCapture(
            str(video_path)
        )

        fps = cap.get(
            cv2.CAP_PROP_FPS
        )

        width = int(
            cap.get(
                cv2.CAP_PROP_FRAME_WIDTH
            )
        )

        height = int(
            cap.get(
                cv2.CAP_PROP_FRAME_HEIGHT
            )
        )

        # =====================================
        # Output Video Path
        # =====================================

        output_path = (
            Path(
                "outputs/processed_videos"
            )
            /
            "processed_video.mp4"
        )

        writer = cv2.VideoWriter(
            str(output_path),
            cv2.VideoWriter_fourcc(
                *"mp4v"
            ),
            fps,
            (width, height)
        )

        frame_count = 0

        # =====================================
        # Process Frames
        # =====================================

        while True:

            success, frame = cap.read()

            if not success:
                break

            frame_count += 1

            results = self.detector.detect(
                frame
            )

            # =====================================
            # Detection Loop
            # =====================================

            for box in results[0].boxes:

                class_id = int(
                    box.cls[0]
                )

                confidence = float(
                    box.conf[0]
                )

                # =====================================
                # Analytics Tracking
                # =====================================

                self.analytics_service.add_detection(
                    class_id
                )

                # =====================================
                # Violation Detection
                # =====================================

                if class_id == 1:

                    if frame_count % 30 == 0:

                        timestamp = (
                            frame_count / fps
                        )

                        self.violation_service.save_violation(
                            frame=frame,
                            frame_number=frame_count,
                            timestamp=round(
                                timestamp,
                                2
                            ),
                            confidence=round(
                                confidence,
                                2
                            )
                        )

            # =====================================
            # Draw Bounding Boxes
            # =====================================

            frame = (
                self.visualizer.draw_boxes(
                    frame,
                    results
                )
            )

            writer.write(frame)

            print(
                f"Frame {frame_count}"
            )

        # =====================================
        # Cleanup Video Resources
        # =====================================

        cap.release()

        writer.release()

        print(
            f"\nSaved: {output_path}"
        )

        # =====================================
        # Violations Summary
        # =====================================

        violations = (
            self.violation_service
            .get_violations()
        )

        print(
            f"\nViolations Found: "
            f"{len(violations)}"
        )

        # =====================================
        # Analytics Generation
        # =====================================

        analytics = (
            self.analytics_service
            .generate_report()
        )

        print(
            "\n========== Analytics Report =========="
        )

        for key, value in analytics.items():

            print(
                f"{key}: {value}"
            )

        # =====================================
        # Save JSON Report
        # =====================================

        report_path = (
            self.report_service
            .save_report(
                analytics
            )
        )

        print(
            f"\nReport Saved: {report_path}"
        )

        # =====================================
        # Save Video Record To Database
        # =====================================

        video_record = (
            self.database_service
            .create_video(
                filename=Path(
                    video_path
                ).name,

                processed_filename=
                    output_path.name,

                total_detections=
                    analytics[
                        "total_detections"
                    ],

                compliance_rate=
                    analytics[
                        "compliance_rate"
                    ]
            )
        )

        print(
            f"\nVideo Record Saved: "
            f"{video_record.id}"
        )

        # =====================================
        # Save Analytics To Database
        # =====================================

        analytics_record = (
    self.database_service
    .create_analytics_report(

        video_id=
            video_record.id,

        total_detections=
            analytics[
                "total_detections"
            ],

        with_helmet=
            analytics[
                "with_helmet"
            ],

        without_helmet=
            analytics[
                "without_helmet"
            ],

        compliance_rate=
            analytics[
                "compliance_rate"
            ],

        violation_rate=
            analytics[
                "violation_rate"
            ]
    )
)

        print(
            f"Analytics Record Saved: "
            f"{analytics_record.id}"
        )

        # =====================================
        # Save Violations To Database
        # =====================================

        for violation in violations:

            self.database_service.create_violation(

                video_id=
                    video_record.id,

                image_path=
                    violation["image"],

                timestamp=
                    violation["timestamp"],

                confidence=
                    violation["confidence"]
            )

        print(
            f"Violation Records Saved: "
            f"{len(violations)}"
        )

        # =====================================
        # Close Database Session
        # =====================================

        self.database_service.close()

        # =====================================
        # Return Processing Results
        # =====================================

        return {

            "analytics":
                analytics,

            "violations":
                violations,

            "report_path":
                str(report_path),

            "processed_video":
                str(output_path),

            "video_id":
                video_record.id
        }