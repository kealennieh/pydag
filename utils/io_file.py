import json


def load_json_file(file_path):
    with open(file_path, "r") as fin:
        json_file = json.load(fin)

    return json_file
