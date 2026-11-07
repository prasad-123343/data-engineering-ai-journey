
import requests


def extract_data():

    url = "https://jsonplaceholder.typicode.com/posts"

    start = 0
    limit = 10

    all_posts = []
    seen_ids = set()

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
            raise ValueError("Expected API response to be a list.")

        if not data:
            print("No more records available.")
            break

        current_ids = [post.get("id") for post in data]

        if any(post_id in seen_ids for post_id in current_ids):
            raise ValueError("Duplicate records detected.")

        all_posts.extend(data)
        seen_ids.update(current_ids)

        print("Records retrieved:", len(data))

        start += len(data)

    print("Total extracted records:", len(all_posts))

    return all_posts
