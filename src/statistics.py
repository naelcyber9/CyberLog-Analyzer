from collections import Counter


def generate_statistics(events, suspects):

    ips = []

    for event in events:
        ips.append(event["ip"])

    counter = Counter(ips)

    stats = {
        "total_events": len(events),
        "unique_ips": len(counter),

        "top_attacker": {
            "ip": counter.most_common(1)[0][0],
            "attempts": counter.most_common(1)[0][1]
        } if counter else None,

        "total_alerts": len(suspects)
    }

    return stats