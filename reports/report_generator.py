import json
from datetime import datetime
from pathlib import Path


def generate_report(results):
    with open(
        "config/security_rules.json",
        "r",
        encoding="utf-8"
    ) as file:
        security_rules = json.load(file)

    lines = []

    lines.append("WINDOWS ENDPOINT SECURITY AUDIT REPORT")
    lines.append("=" * 45)
    lines.append(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    lines.append("")

    total_checks = len(results)

    passed_checks = sum(
        1
        for result in results
        if result["result"] == "PASS"
    )

    failed_checks = sum(
        1
        for result in results
        if result["result"] == "FAIL"
    )

    lines.append("AUDIT SUMMARY")
    lines.append("-" * 13)
    lines.append(f"Total checks: {total_checks}")
    lines.append(f"Passed: {passed_checks}")
    lines.append(f"Failed: {failed_checks}")
    lines.append("")

    lines.append("DETAILED RESULTS")
    lines.append("=" * 45)
    lines.append("")

    for result in results:
        rule = security_rules[result["id"]]

        explanation = result.get(
            "explanation",
            rule["explanation"]
        )

        severity = result.get(
            "severity",
            rule["severity"]
        )

        risk = result.get(
            "risk",
            rule["risk"]
        )

        remediation = result.get(
            "remediation",
            rule["remediation"]
        )

        lines.append(result["name"])
        lines.append("-" * len(result["name"]))

        lines.append(f"Explanation: {explanation}")
        lines.append("")
        lines.append(f'Expected: {result["expected"]}')
        lines.append(f'Actual: {result["actual"]}')
        lines.append(f'Result: {result["result"]}')
        lines.append(f"Severity: {severity}")
        lines.append("")

        if result["result"] == "FAIL":
            lines.append(
                f"Security Risk: {risk}"
            )

            lines.append(
                f"Recommended Action: {remediation}"
            )

        else:
            lines.append(
                "Assessment: The current configuration matches "
                "the expected security baseline."
            )

            lines.append(
                f"Risk if Misconfigured: {risk}"
            )

            lines.append(
                "Recommended Action: No immediate remediation "
                f"is required. Maintain the expected secure state. "
                f"{remediation}"
            )

        lines.append("")
        lines.append("=" * 45)
        lines.append("")

    report_text = "\n".join(lines)

    output_directory = Path(
        "reports/generated"
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = (
        "security_audit_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".txt"
    )

    output_path = output_directory / filename

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report_text)

    return report_text, output_path