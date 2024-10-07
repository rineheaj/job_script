import json

##LOAD DATA
def load_json_data():
    try:
        with open("job_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# SAVE DATA
def save_json_data(data):
    with open("job_data.json", "w") as f:
        json.dump(data, f, indent=4)