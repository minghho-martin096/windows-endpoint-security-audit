import json
import subprocess


def check_defender_realtime():
    with open("config/baseline.json", "r") as file:
        baseline = json.load(file)

    expected = baseline["defender_realtime_protection_enabled"]

    result = subprocess.run(
        [
            "powershell",
            "-Command",
            "(Get-MpComputerStatus).RealTimeProtectionEnabled"
        ],
        capture_output=True,
        text=True
    )

    actual = result.stdout.strip().lower() == "true"

    status = "PASS" if actual == expected else "FAIL"

    print("\nDefender Real-Time Protection")
    print(f"Expected: {'Enabled' if expected else 'Disabled'}")
    print(f"Actual: {'Enabled' if actual else 'Disabled'}")
    print(f"Result: {status}")