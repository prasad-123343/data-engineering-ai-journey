
import time

for attempt in range(1, 4):
    try:
        print("Attempt:", attempt)
        raise ConnectionError("API failed")

    except ConnectionError:
        print("API failed, retrying...")
        if attempt < 3:
            delay = 2 ** (attempt - 1)
            print(f"Waiting {delay} seconds...")
            time.sleep(delay)
else:
    print("API failed after 3 attempts")

