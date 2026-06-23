from app.database.database import (
    SessionLocal
)

from app.database.models import (
    Video,
    Violation,
    AnalyticsReport
)


class DatabaseService:

    def __init__(self):

        self.db = SessionLocal()

    # =====================================
    # VIDEO
    # =====================================

    def create_video(
        self,
        filename,
        processed_filename,
        total_detections,
        compliance_rate
    ):

        video = Video(
            filename=filename,
            processed_filename=processed_filename,
            total_detections=total_detections,
            compliance_rate=compliance_rate
        )

        self.db.add(video)

        self.db.commit()

        self.db.refresh(video)

        return video

    # =====================================
    # VIOLATIONS
    # =====================================

    def create_violation(
        self,
        video_id,
        image_path,
        timestamp,
        confidence
    ):

        violation = Violation(
            video_id=video_id,
            image_path=image_path,
            timestamp=timestamp,
            confidence=confidence
        )

        self.db.add(violation)

        self.db.commit()

        self.db.refresh(violation)

        return violation

    # =====================================
    # ANALYTICS
    # =====================================

    def create_analytics_report(
        self,
        video_id,
        total_detections,
        with_helmet,
        without_helmet,
        compliance_rate,
        violation_rate
    ):

        report = AnalyticsReport(

            video_id=video_id,

            total_detections=total_detections,

            with_helmet=with_helmet,

            without_helmet=without_helmet,

            compliance_rate=compliance_rate,

            violation_rate=violation_rate
        )

        self.db.add(report)

        self.db.commit()

        self.db.refresh(report)

        return report

    # =====================================
    # CLOSE SESSION
    # =====================================

    def close(self):

        self.db.close()