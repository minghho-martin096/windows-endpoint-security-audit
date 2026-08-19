from checks.firewall import check_firewall
from checks.defender import check_defender
from checks.defender_realtime import check_defender_realtime

check_firewall()
check_defender()
check_defender_realtime()