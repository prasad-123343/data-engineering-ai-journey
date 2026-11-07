
import requests
import json
import os

# Step 1: API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Step 2: Create two empty lists
valid_records = []
rejected_records = []

try:
    # Step 3: Fetch records
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    posts = response.json()

    # Step 4: Validate every API record
    for post in posts:

        rejection_reasons = []

        # Rule 1: userId must be an integer
        if type(post.get("userId")) is not int:
            rejection_reasons.append(
                "userId must be an integer"
            )

        # Rule 2: id must be an integer
        if type(post.get("id")) is not int:
            rejection_reasons.append(
                "id must be an integer"
            )

        # Rule 3: title must be a non-empty string
        if (
            not isinstance(post.get("title"), str)
            or not post.get("title").strip()
        ):
            rejection_reasons.append(
                "title must be a non-empty string"
            )

        # Rule 4: body must be a non-empty string
        if (
            not isinstance(post.get("body"), str)
            or not post.get("body").strip()
        ):
            rejection_reasons.append(
                "body must be a non-empty string"
            )

        # Step 5: Separate valid and rejected records
        if len(rejection_reasons) == 0:
            valid_records.append(post)

        else:
            rejected_records.append({
                "record": post,
                "rejection_reasons": rejection_reasons
            })

    # Step 6: Test an invalid record
    print("\n========== TEST INVALID RECORD ==========")

    test_post = {
        "userId": 1,
        "id": 101,
        "title": "",
        "body": "This is a test record."
    }

    test_rejection_reasons = []

    if type(test_post.get("userId")) is not int:
        test_rejection_reasons.append(
            "userId must be an integer"
        )

    if type(test_post.get("id")) is not int:
        test_rejection_reasons.append(
            "id must be an integer"
        )

    if (
        not isinstance(test_post.get("title"), str)
        or not test_post.get("title").strip()
    ):
        test_rejection_reasons.append(
            "title must be a non-empty string"
        )

    if (
        not isinstance(test_post.get("body"), str)
        or not test_post.get("body").strip()
    ):
        test_rejection_reasons.append(
            "body must be a non-empty string"
        )

    if test_rejection_reasons:
        print("Rejected record:", test_post)
        print("Rejection reasons:", test_rejection_reasons)
    else:
        print("Valid record")

    # Step 7: Create output directory
    os.makedirs("day13/output", exist_ok=True)

    # Step 8: Save valid records into JSON
    with open(
        "day13/output/valid_posts.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(valid_records, file, indent=4)

    # Step 9: Save rejected records into JSON
    with open(
        "day13/output/rejected_posts.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(rejected_records, file, indent=4)

    print("\nJSON files saved successfully!")

    # Step 10: Print validation summary
    print("\n========== API DATA VALIDATION SUMMARY ==========")
    print("Total API Records:", len(posts))
    print("Valid API Records:", len(valid_records))
    print("Rejected API Records:", len(rejected_records))

    # Step 11: Display rejected API records
    print("\nREJECTED API RECORDS")

    for rejected in rejected_records:
        print("Record:", rejected["record"])
        print("Reasons:", rejected["rejection_reasons"])

    print("\nOutput files:")
    print("day13/output/valid_posts.json")
    print("day13/output/rejected_posts.json")

except requests.exceptions.RequestException as error:
    print("API request failed:", error)

except (ValueError, OSError) as error:
    print("Data processing or file error:", error)
