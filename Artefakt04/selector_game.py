import json

with open("miner_report.json") as f:
    data = json.load(f)

user_id = input("Podaj id: ")
user_tag = input("Podaj tag: ")

matches = []

for elem in data:
    if elem["id"] == user_id and elem["tag"] == user_tag:
        matches.append(elem)

print("Znaleziono", len(matches), "dopasowan")

if len(matches) == 1:
    print("STATUS: ZALICZONE! Twoj selektor jest unikalny.")
else:
    print("Selektor nie jest unikalny.")