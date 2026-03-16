import xml.etree.ElementTree as ET
import glob
import json
from collections import Counter

def analyze_stability(path):

    tags = []

    for file in glob.glob(path + "/**/*.xml", recursive=True):

        try:
            tree = ET.parse(file)

            for elem in tree.iter():
                tag = elem.tag.split("}")[-1]
                tags.append(tag)

        except:
            pass

    counter = Counter(tags)
    total = sum(counter.values())

    report = {
        "metrics": {},
        "verdict": "LOW_RISK",
        "warnings": []
    }

    threshold = 0.5   # 50%

    for cls, count in counter.items():

        percentage = round((count / total) * 100, 2)

        report["metrics"][cls] = {
            "count": count,
            "percentage": percentage
        }

        if percentage > threshold * 100:
            report["verdict"] = "HIGH_RISK"
            report["warnings"].append(
                f"{cls} dominates UI ({percentage}%). Avoid By.className!"
            )

    with open("stability_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print(f"Audit Complete. Verdict: {report['verdict']}")

analyze_stability("../Artefakt02/decompiled_apk/res/layout")