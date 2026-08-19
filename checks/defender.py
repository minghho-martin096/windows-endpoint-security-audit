import json
import subprocess


def check_defender():
    with open("config/baseline.json", "r") as file:
        baseline = json.load(file)

    expected = baseline["microsoft_defender_enabled"]

    result = subprocess.run(
        [
            "powershell",
            "-Command",
            "(Get-MpComputerStatus).AntivirusEnabled"
        ],
        capture_output=True,
        text=True
    )

    actual = result.stdout.strip().lower() == "true"

    status = "PASS" if actual == expected else "FAIL"

    print("\nMicrosoft Defender")
    print(f"Expected: {'Enabled' if expected else 'Disabled'}")
    print(f"Actual: {'Enabled' if actual else 'Disabled'}")
    print(f"Result: {status}")