
import requests

url = "https://jsonplaceholder.typicode.com/posts"

page = 1
start = 0
limit = 10

seen_ids = set()
total_records = 0

try:
    while True:

        params = {
            "_start": start,
            "_limit": limit
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            print("Error: Expected a list of records.")
            break

        if not data:
            print("\nNo more records available.")
            break

        # Detect repeated records to prevent an infinite loop
        current_ids = [post["id"] for post in data]

        if any(post_id in seen_ids for post_id in current_ids):
            print("\nRepeated records detected.")
            print("Stopping pagination to prevent duplicate processing.")
            break

        print(f"\n========== PAGE {page} ==========")

        for post in data:
            print(
                "Post ID:", post["id"],
                "| User ID:", post["userId"]
            )

        print("Records received:", len(data))

        seen_ids.update(current_ids)
        total_records += len(data)

        # Move to the next batch
        start += len(data)
        page += 1

    print("\n========== PAGINATION SUMMARY ==========")
    print("Total unique records:", len(seen_ids))
    print("Total records processed:", total_records)

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
