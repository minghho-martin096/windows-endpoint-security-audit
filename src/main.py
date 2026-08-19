from checks.firewall import check_firewall
from checks.defender import check_defender
from checks.defender_realtime import check_defender_realtime
from checks.guest_account import check_guest_account

check_firewall()
check_defender()
check_defender_realtime()
check_guest_account()