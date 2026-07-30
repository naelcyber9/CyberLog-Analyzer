import re


def extract_ip(line):

    pattern = r"\d+\.\d+\.\d+\.\d+"

    result = re.search(pattern, line)

    if result:
        return result.group()

    return None


def extract_time(line):

    pattern = r"^\w+\s+\d+\s+\d+:\d+:\d+"

    result = re.search(pattern, line)

    if result:
        return result.group()

    return None

def extract_port(line):

    pattern = r"port\s+(\d+)"

    result = re.search(pattern, line)

    if result:
        return result.group(1)

    return None

def parse_file(filepath):

    events = []

    with open(filepath, "r") as file:

        for line in file:

            ip = extract_ip(line)
            time = extract_time(line)
            port = extract_port(line)

            if ip and time:
                event = {
                    "ip": ip,
                    "time": time
                }

                if port:
                    event["port"] = port

                events.append(event)

    return events