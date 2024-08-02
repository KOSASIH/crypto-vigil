import os
import json
import datetime
from jinja2 import Environment, FileSystemLoader
from penetration_testing.test_manager import TestManager

class ReportGenerator:
    def __init__(self, test_manager: TestManager):
        self.test_manager = test_manager
        self.report_dir = "reports"
        self.template_dir = "templates"
        self.template_env = Environment(loader=FileSystemLoader(self.template_dir))

    def generate_report(self, target: str, test_type: str, test_results: dict) -> str:
        """
        Generates a report for the given target and test type.

        Args:
            target (str): Target system (e.g. IP address, hostname)
            test_type (str): Type of test (e.g. network, web, os)
            test_results (dict): Test results

        Returns:
            str: Report file path
        """
        report_template = self.template_env.get_template("report.html")
        report_data = self._prepare_report_data(target, test_type, test_results)
        report_html = report_template.render(report_data)
        report_file_path = self._save_report(report_html, target, test_type)
        return report_file_path

    def _prepare_report_data(self, target: str, test_type: str, test_results: dict) -> dict:
        """
        Prepares the report data for the given target and test type.

        Args:
            target (str): Target system (e.g. IP address, hostname)
            test_type (str): Type of test (e.g. network, web, os)
            test_results (dict): Test results

        Returns:
            dict: Report data
        """
        report_data = {
            "target": target,
            "test_type": test_type,
            "test_results": test_results,
            "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return report_data

    def _save_report(self, report_html: str, target: str, test_type: str) -> str:
        """
        Saves the report to a file.

        Args:
            report_html (str): Report HTML content
            target (str): Target system (e.g. IP address, hostname)
            test_type (str): Type of test (e.g. network, web, os)

        Returns:
            str: Report file path
        """
        report_file_name = f"{target}_{test_type}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
        report_file_path = os.path.join(self.report_dir, report_file_name)
        with open(report_file_path, "w") as f:
            f.write(report_html)
        return report_file_path

def main():
    test_manager = TestManager()
    report_generator = ReportGenerator(test_manager)
    target = "192.168.1.1"
    test_type = "network"
    test_results = test_manager.run_test(target, test_type)
    report_file_path = report_generator.generate_report(target, test_type, test_results)
    print(f"Report generated: {report_file_path}")

if __name__ == "__main__":
    main()
