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

    print("\nGuest Account")
    print(f"Expected: {'Enabled' if expected else 'Disabled'}")
    print(f"Actual: {'Enabled' if actual else 'Disabled'}")
    print(f"Result: {status}")