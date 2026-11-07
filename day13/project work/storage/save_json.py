import json
from pathlib import Path


def save_json(valid_posts, rejected_posts):

    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    valid_file = output_folder / "valid_posts.json"
    rejected_file = output_folder / "rejected_posts.json"

    with open(valid_file, "w", encoding="utf-8") as file:
        json.dump(valid_posts, file, indent=4)

    with open(rejected_file, "w", encoding="utf-8") as file:
        json.dump(rejected_posts, file, indent=4)

    print("Valid records saved:", valid_file)
    print("Rejected records saved:", rejected_file)