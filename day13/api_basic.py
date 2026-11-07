
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)

    print("\nResponse URL:")
    print(response.url)

    print("\nResponse Headers:")
    print(response.headers)

    print("\nResponse Body:")
    print(response.text[:500])

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
