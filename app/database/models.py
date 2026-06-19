from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    DeclarativeBase,
    relationship
)


# ==========================================================
# Base Class
# ==========================================================

class Base(DeclarativeBase):
    pass


# ==========================================================
# Videos Table
# ==========================================================

class Video(Base):

    __tablename__ = "videos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String,
        nullable=False
    )

    processed_filename = Column(
        String,
        nullable=True
    )

    upload_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    processing_time = Column(
        Float,
        nullable=True
    )

    total_detections = Column(
        Integer,
        default=0
    )

    compliance_rate = Column(
        Float,
        default=0.0
    )

    violation_rate = Column(
        Float,
        default=0.0
    )

    # Relationships

    violations = relationship(
        "Violation",
        back_populates="video",
        cascade="all, delete-orphan"
    )

    analytics_report = relationship(
        "AnalyticsReport",
        back_populates="video",
        uselist=False,
        cascade="all, delete-orphan"
    )

    def __repr__(self):

        return (
            f"<Video("
            f"id={self.id}, "
            f"filename='{self.filename}'"
            f")>"
        )


# ==========================================================
# Violations Table
# ==========================================================

class Violation(Base):

    __tablename__ = "violations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    video_id = Column(
        Integer,
        ForeignKey("videos.id"),
        nullable=False
    )

    image_path = Column(
        String,
        nullable=False
    )

    timestamp = Column(
        Float,
        nullable=False
    )

    confidence = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationship

    video = relationship(
        "Video",
        back_populates="violations"
    )

    def __repr__(self):

        return (
            f"<Violation("
            f"id={self.id}, "
            f"timestamp={self.timestamp}"
            f")>"
        )


# ==========================================================
# Analytics Reports Table
# ==========================================================

class AnalyticsReport(Base):

    __tablename__ = "analytics_reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    video_id = Column(
        Integer,
        ForeignKey("videos.id"),
        unique=True,
        nullable=False
    )

    total_detections = Column(
        Integer,
        default=0
    )

    with_helmet = Column(
        Integer,
        default=0
    )

    without_helmet = Column(
        Integer,
        default=0
    )

    compliance_rate = Column(
        Float,
        default=0.0
    )

    violation_rate = Column(
        Float,
        default=0.0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationship

    video = relationship(
        "Video",
        back_populates="analytics_report"
    )

    def __repr__(self):

        return (
            f"<AnalyticsReport("
            f"id={self.id}, "
            f"compliance_rate={self.compliance_rate}"
            f")>"
        )