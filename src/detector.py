from collections import Counter

def calculate_severity(attempts):

    if attempts >= 20:
        return "CRITICAL"

    elif attempts >= 11:
        return "HIGH"

    elif attempts >= 6:
        return "MEDIUM"

    else:
        return "LOW"

def detect_bruteforce(events, threshold):

    ips = []

    for event in events:
        ips.append(event["ip"])

    counter = Counter(ips)

    alerts = []

    for ip, count in counter.items():

        if count > threshold:
            alerts.append({
                "ip": ip,
                "attack": "SSH Brute Force",
                "attempts": count,
                "severity": calculate_severity(count)
            })

    return alerts