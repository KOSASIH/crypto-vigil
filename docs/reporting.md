# Reporting
==========

The reporting component generates reports for penetration tests.

### Report Generator

The report generator takes in the test results and generates a report in HTML format. The report includes the following information:

* Target system information
* Test type and results
* Generated at timestamp

### Configuration

The report generator can be configured using the following settings:

* `REPORT_DIR`: The directory where the reports will be saved
* `TEMPLATE_DIR`: The directory where the report templates are located

### Usage

To use the report generator, follow these steps:

1. Run the test using the `TestManager` class
2. Pass the test results to the `ReportGenerator` class
3. Call the `generate_report` method to generate the report

### Example

```python
from reporting.report_generator import ReportGenerator
from penetration_testing.test_manager import TestManager

test_manager = TestManager()
report_generator = ReportGenerator(test_manager)
target = "192.168.1.1"
test_type = "network"
test_results = test_manager.run_test(target, test_type)
report_file_path = report_generator.generate_report(target, test_type, test_results)
print(f"Report generated: {report_file_path}")
