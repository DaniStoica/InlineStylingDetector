import json
import os
from bs4 import BeautifulSoup

htmlFiles = []
jsonExport = []


def parse_html_files(html_file):
    with open(html_file, encoding="ISO-8859-1") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        tags = soup.find_all(style=True)
        jsonExport.append({
            "name": "Inline Styling",
            "category": "Code Style",
            "file": os.path.join(root, file).removeprefix(dirPath).removeprefix("\\").replace("\\", "/"),
            "value": str(tags).count("style")
        })


print("Give project directory name: ")
dirPath = str(input())
if os.path.exists(dirPath):
    print("Parse started...")
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            if file.endswith(".html"):
                parse_html_files(os.path.join(root, file))
    with open('result.json', 'w') as json_file:
        json.dump(jsonExport, json_file)
        print("Process finished. See results in results.json file.")
else:
    print("Wrong Path!")
