from datetime import datetime
from pathlib import Path


def generate_report(results):
    lines = []

    lines.append("WINDOWS ENDPOINT SECURITY AUDIT REPORT")
    lines.append("=" * 45)
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    for result in results:
        lines.append(result["name"])
        lines.append("-" * len(result["name"]))
        lines.append(f'Expected: {result["expected"]}')
        lines.append(f'Actual: {result["actual"]}')
        lines.append(f'Result: {result["result"]}')
        lines.append("")

    report_text = "\n".join(lines)

    output_directory = Path("reports/generated")
    output_directory.mkdir(parents=True, exist_ok=True)

    filename = (
        "security_audit_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".txt"
    )

    output_path = output_directory / filename

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return report_text, output_path