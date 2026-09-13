from src.audit_service import run_audit
from reports.report_generator import generate_report


results = run_audit()

report, report_path = generate_report(results)

print(report)
print(f"Report saved to: {report_path}")