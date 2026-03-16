import xml.etree.ElementTree as ET
import glob
import json

def mine_selectors(path):

    results = []

    for file in glob.glob(path + "/**/*.xml", recursive=True):
        tree = ET.parse(file)

        for elem in tree.iter():

            res_id = elem.get('{http://schemas.android.com/apk/res/android}id')

            if res_id:
                record = {
                    "file": file,
                    "id": res_id.split("/")[-1],
                    "tag": elem.tag
                }

                results.append(record)

    with open("miner_report.json","w") as f:
        json.dump(results,f,indent=4)

mine_selectors("../app/res/layout")