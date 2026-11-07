
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    print("Connecting to API...")

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    print("API request successful!")
    print("Total records:", len(data))

except requests.exceptions.Timeout:
    print("Error: API request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the API.")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.JSONDecodeError:
    print("Error: Invalid JSON response.")

except requests.exceptions.RequestException as error:
    print("Request error:", error)
