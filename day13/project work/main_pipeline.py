from ingestion.extract import extract_data
from processing.validate import validate_data
from storage.save_json import save_json
from storage.load_sqlite import load_to_sqlite
from analytics.run_queries import run_sql_queries


def main():

    print("\n========== DATA ENGINEERING PIPELINE STARTED ==========\n")

    # Step 1: Extract
    print("STEP 1: EXTRACTING DATA")
    posts = extract_data()

    # Step 2: Validate
    print("\nSTEP 2: VALIDATING DATA")
    valid_posts, rejected_posts = validate_data(posts)

    # Step 3: Save JSON
    print("\nSTEP 3: SAVING JSON FILES")
    save_json(valid_posts, rejected_posts)

    # Step 4: Load SQLite
    print("\nSTEP 4: LOADING DATA INTO SQLITE")
    load_to_sqlite()

    # Step 5: Run analytics
    print("\nSTEP 5: RUNNING SQL ANALYTICS")
    run_sql_queries()

    print("\n========== DATA ENGINEERING PIPELINE COMPLETED ==========\n")


if __name__ == "__main__":
    main()