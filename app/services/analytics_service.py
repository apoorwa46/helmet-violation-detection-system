# Collects detection totals and converts them into simple compliance metrics.
# Class ID 0 represents a rider with a helmet; every other ID is currently
# treated as a rider without a helmet, matching the detector's class setup.
class AnalyticsService:
    def __init__(self):
        # These counters live for the lifetime of this service instance.
        self.with_helmet_count=0
        self.without_helmet_count=0
        self.total_detections=0

    def add_detection(self,class_id):
        # Count every detected object before placing it in a class bucket.
        self.total_detections += 1
        if class_id == 0:
            self.with_helmet_count += 1
        else:
            self.without_helmet_count += 1

    def generate_report(self):

        # Avoid dividing by zero when no frames have produced detections.
        if self.total_detections == 0:

            compliance_rate = 0

            violation_rate = 0

        else:

            # Express each class count as a percentage of all detections.
            compliance_rate = (
                self.with_helmet_count
                /
                self.total_detections
            ) * 100

            violation_rate = (
                self.without_helmet_count
                /
                self.total_detections
            ) * 100

        # Round percentages for a cleaner JSON report and console display.
        return {

            "total_detections":
                self.total_detections,

            "with_helmet":
                self.with_helmet_count,

            "without_helmet":
                self.without_helmet_count,

            "compliance_rate":
                round(
                    compliance_rate,
                    2
                ),

            "violation_rate":
                round(
                    violation_rate,
                    2
                )
        }
