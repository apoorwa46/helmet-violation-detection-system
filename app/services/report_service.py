import json

from pathlib import Path


class ReportService:

    def __init__(self):

        # Keep generated analytics reports in one predictable project folder.
        self.report_dir = Path(
            "outputs/reports"
        )

        # Create the folder on first use; exist_ok keeps later runs harmless.
        self.report_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_report(
        self,
        report
    ):

        # Each run updates the same report file with the latest analytics.
        output_file = (
            self.report_dir
            /
            "analytics_report.json"
        )

        # Pretty-print the dictionary as JSON so the report is easy to inspect.
        with open(
            output_file,
            "w"
        ) as f:

            json.dump(
                report,
                f,
                indent=4
            )

        # Return the Path so callers can display it or include it in a response.
        return output_file
