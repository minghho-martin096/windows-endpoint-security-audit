from checks.firewall import check_firewall
from checks.defender import check_defender
from checks.defender_realtime import check_defender_realtime
from checks.guest_account import check_guest_account
from reports.report_generator import generate_report


results = [
    check_firewall(),
    check_defender(),
    check_defender_realtime(),
    check_guest_account()
]


report, report_path = generate_report(results)

print(report)
print(f"Report saved to: {report_path}")