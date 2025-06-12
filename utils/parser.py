import re
from collections import defaultdict
from datetime import datetime

def parse_auth_log(log_text):
    failed_logins = []
    brute_force_ips = defaultdict(int)

    for line in log_text.splitlines():
        # Match failed login attempts
        match = re.search(r'Failed password for .* from ([\d.]+) port', line)
        if match:
            ip = match.group(1)
            brute_force_ips[ip] += 1
            failed_logins.append((ip, line))

    # Detect brute force (e.g., >5 attempts)
    brute_force_summary = {ip: count for ip, count in brute_force_ips.items() if count > 5}

    return failed_logins, brute_force_summary
