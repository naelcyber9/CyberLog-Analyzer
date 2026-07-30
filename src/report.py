def generate_report(suspects, events, stats):

    with open("reports/security_report.txt", "w") as report:

        report.write("========== SECURITY REPORT ==========\n\n")

        report.write("========== STATISTICS ==========\n\n")

        report.write(f"Total events analyzed : {stats['total_events']}\n")
        report.write(f"Unique IP addresses : {stats['unique_ips']}\n")

        if stats["top_attacker"]:
            ip = stats["top_attacker"]["ip"]
            count = stats["top_attacker"]["attempts"]
            report.write(f"Top attacker : {ip} ({count} attempts)\n")

        report.write(f"Total alerts : {stats['total_alerts']}\n\n")



        report.write("========== ALERTS ==========\n\n")


        if not suspects:
            report.write("No threats detected.\n")
            return

        for suspect in suspects:

            ip = suspect["ip"]
            severity = suspect["severity"]

            report.write("Threat : SSH Brute Force\n")
            report.write(f"IP Address : {ip}\n")

            if suspect["attack"] == "SSH Brute Force":

                report.write(f"Attempts  : {suspect['attempts']}\n")
            
            elif suspect["attack"] == "Port Scan":

                report.write(f"Ports scanned : {suspect['ports_scanned']}\n")
            
            report.write(f"Severity : {severity}\n\n")
            
            for event in events:

                if event["ip"] == ip:
                    report.write(f" - {event['time']}\n")

            report.write("\n------------------------------------\n\n")


    print("Report generated : reports/security_report.txt")