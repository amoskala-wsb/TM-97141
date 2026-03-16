import xml.etree.ElementTree as ET
import glob
import json

results = []

for file in glob.glob("../App/res/layout/**/*.xml", recursive=True):

    try:
        tree = ET.parse(file)

        for elem in tree.iter():

            text = elem.get('{http://schemas.android.com/apk/res/android}text')
            desc = elem.get('{http://schemas.android.com/apk/res/android}contentDescription')

            if text and not desc:

                results.append({
                    "file": file.split("/")[-1],
                    "tag": elem.tag.split("}")[-1],
                    "text": text
                })

    except:
        pass

with open("a11y_report.json","w") as f:
    json.dump(results,f,indent=4)

print("Raport zapisany do a11y_report.json")