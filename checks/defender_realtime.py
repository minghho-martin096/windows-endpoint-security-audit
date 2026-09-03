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

    return {
        "id": "defender_realtime_protection_enabled",
        "name": "Defender Real-Time Protection",
        "expected": "Enabled" if expected else "Disabled",
        "actual": "Enabled" if actual else "Disabled",
        "result": status
    }