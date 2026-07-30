import json


def export_json(suspects, stats):

    data = {
        "statistics": stats,
        "alerts": suspects
    }

    with open("reports/security_report.json", "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

    print("JSON report generated : reports/security_report.json")