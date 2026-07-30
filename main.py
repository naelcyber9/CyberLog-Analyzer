import sys

from src.parser import parse_file
from src.detector import detect_bruteforce
from src.port_scanner import detect_port_scan
from src.statistics import generate_statistics
from src.report import generate_report
from src.exporter import export_json


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <log_file>")
        return

    log_file = sys.argv[1]

    events = parse_file(log_file)

    bruteforce_alerts = detect_bruteforce(events, threshold=3)

    portscan_alerts = detect_port_scan(events)

    all_alerts = bruteforce_alerts + portscan_alerts

    stats = generate_statistics(events, all_alerts)

    generate_report(all_alerts, events, stats)

    export_json(all_alerts, stats)

    print("Analysis completed successfully.")


if __name__ == "__main__":
    main()