import json
import subprocess


def check_guest_account():
    with open("config/baseline.json", "r") as file:
        baseline = json.load(file)

    expected = baseline["guest_account_enabled"]

    result = subprocess.run(
        [
            "powershell",
            "-Command",
            "(Get-LocalUser -Name 'Guest').Enabled"
        ],
        capture_output=True,
        text=True
    )

    actual = result.stdout.strip().lower() == "true"

    status = "PASS" if actual == expected else "FAIL"

    return {
        "id": "guest_account_enabled",
        "name": "Guest Account",
        "expected": "Enabled" if expected else "Disabled",
        "actual": "Enabled" if actual else "Disabled",
        "result": status
    }