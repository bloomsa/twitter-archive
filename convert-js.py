# Converts js data files in the export into usable json files
import json
import re
import os

from pathlib import Path

data_path = "/Users/sambloomquist/projects/twitter-archive/export/data"

json_path = f"{data_path}/json"

for js_file in Path(data_path).glob("*.js"):
    with open(js_file, "r") as file:
        file_content = file.read()
        match = re.search(r"window\.YTD\.(?:[^.]+)\.part0\s*=\s*(\[.*\])", file_content, re.DOTALL)
        if match:
            json_string = match.group(1)
            json_data = json.loads(json_string)
            with open(f"{json_path}/{js_file.stem}.json", "w") as json_file:
                json.dump(json_data, json_file, indent=4)
                os.remove(js_file)
                print(f"Converted and deleted {js_file.stem}.js")

        else:
           print("No match found.")