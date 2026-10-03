
import time

for attempt in range(1, 4):
    try:
        print("Attempt:", attempt)

        if attempt < 3:
            raise ConnectionError("API failed")

        print("API succeeded")
        break

    except ConnectionError:
        print("API failed, retrying...")

        if attempt < 3:
            delay = 2 ** (attempt - 1)
            print(f"Waiting {delay} seconds...")
            time.sleep(delay)

print("Pipeline finished")