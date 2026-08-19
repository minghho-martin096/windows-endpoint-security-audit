import json
import subprocess


def check_firewall():
    with open("config/baseline.json", "r") as file:
        baseline = json.load(file)

    expected = baseline["windows_firewall_enabled"]

    result = subprocess.run(
        [
            "powershell",
            "-Command",
            "Get-NetFirewallProfile | Select-Object -ExpandProperty Enabled"
        ],
        capture_output=True,
        text=True
    )

    states = result.stdout.strip().splitlines()

    actual = all(
        state.strip().lower() == "true"
        for state in states
    )

    status = "PASS" if actual == expected else "FAIL"

    print("Windows Firewall")
    print(f"Expected: {'Enabled' if expected else 'Disabled'}")
    print(f"Actual: {'Enabled' if actual else 'Disabled'}")
    print(f"Result: {status}")