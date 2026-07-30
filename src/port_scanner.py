from collections import defaultdict


def detect_port_scan(events, threshold=5):

    ports_by_ip = defaultdict(set)

    for event in events:

        if "port" in event:

            ports_by_ip[event["ip"]].add(event["port"])


    alerts = []


    for ip, ports in ports_by_ip.items():

        if len(ports) >= threshold:

            alerts.append({
                "ip": ip,
                "attack": "Port Scan",
                "ports_scanned": len(ports),
                "severity": "HIGH"
            })


    return alerts
