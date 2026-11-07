
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Step 1: Send API request
    response = requests.get(url, timeout=10)

    if response.status_code == 200:

        # Step 2: Convert JSON response into Python data
        data = response.json()

        print("Total records:", len(data))

        # Step 3: Process every post
        print("\n========== POST DETAILS ==========")

        for post in data:

            user_id = post["userId"]
            post_id = post["id"]
            title = post["title"]

            print("User ID:", user_id)
            print("Post ID:", post_id)
            print("Title:", title)
            print("----------------------------")

        # Step 4: Count posts by user
        post_count_by_user = {}

        for post in data:

            user_id = post["userId"]

            if user_id in post_count_by_user:
                post_count_by_user[user_id] += 1
            else:
                post_count_by_user[user_id] = 1

        # Step 5: Display aggregation results
        print("\n========== POSTS BY USER ==========")

        for user_id, count in post_count_by_user.items():

            print(
                "User ID:", user_id,
                "| Post Count:", count
            )

    else:
        print("API request failed:", response.status_code)

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
