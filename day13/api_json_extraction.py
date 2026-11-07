
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:

        data = response.json()

        print("Data successfully retrieved.")

        print("Data type:", type(data))

        print("Total records:", len(data))

        print("\nFirst record:")
        print(data[0])

        print("\nFirst record title:")
        print(data[0]["title"])

    else:
        print("API request failed.")
        print("Status code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
