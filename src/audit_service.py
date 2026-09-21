import json

from checks.firewall import check_firewall
from checks.defender import check_defender
from checks.defender_realtime import check_defender_realtime
from checks.guest_account import check_guest_account


def run_audit():
    with open("config/security_rules.json", "r") as file:
        security_rules = json.load(file)

    results = [
        check_firewall(),
        check_defender(),
        check_defender_realtime(),
        check_guest_account()
    ]

    for result in results:
        rule = security_rules[result["id"]]

        result["severity"] = rule["severity"]

        if result["result"] == "FAIL":
            result["risk"] = rule["risk"]
            result["remediation"] = rule["remediation"]
        else:
            result["risk"] = ""
            result["remediation"] = ""

    return results