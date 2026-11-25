
import boto3
import csv
import io

# AWS configuration
BUCKET_NAME = "prasad-de-apprenticeship-2026"
REGION = "ap-southeast-2"

# Create S3 client using AWS CLI login credentials
s3_client = boto3.client(
    "s3",
    region_name=REGION
)


# STEP 1: EXTRACT - Read CSV directly from S3
response = s3_client.get_object(
    Bucket=BUCKET_NAME,
    Key="raw/customers.csv"
)

csv_file = io.TextIOWrapper(
    response["Body"],
    encoding="utf-8"
)

reader = csv.DictReader(csv_file)


# STEP 2: TRANSFORM - Validate customer records
valid_records = []
rejected_records = []

for row in reader:
    if (
        row["customer_id"].strip()
        and row["name"].strip()
        and row["city"].strip()
    ):
        valid_records.append(row)
    else:
        rejected_records.append(row)

csv_file.close()


# STEP 3: DISPLAY - Print validation results
total_records = len(valid_records) + len(rejected_records)

print("ETL VALIDATION SUMMARY")
print("----------------------")
print("Total records:", total_records)
print("Valid records:", len(valid_records))
print("Rejected records:", len(rejected_records))


# STEP 4: TRANSFORM - Convert Python records into CSV bytes
def convert_to_csv(records):
    output = io.StringIO()

    fieldnames = ["customer_id", "name", "city"]

    writer = csv.DictWriter(
        output,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(records)

    return output.getvalue().encode("utf-8")


valid_csv = convert_to_csv(valid_records)
rejected_csv = convert_to_csv(rejected_records)


# STEP 5: LOAD - Upload valid records to processed/
s3_client.put_object(
    Bucket=BUCKET_NAME,
    Key="processed/customers.csv",
    Body=valid_csv,
    ContentType="text/csv"
)


# STEP 6: LOAD - Upload rejected records to rejected/
s3_client.put_object(
    Bucket=BUCKET_NAME,
    Key="rejected/rejected_customers.csv",
    Body=rejected_csv,
    ContentType="text/csv"
)


# STEP 7: DISPLAY - Upload summary
print("\nS3 UPLOAD SUMMARY")
print("-----------------")
print("Valid records uploaded:", len(valid_records))
print("Rejected records uploaded:", len(rejected_records))
print("Processed file: s3://{}/processed/customers.csv".format(BUCKET_NAME))
print("Rejected file: s3://{}/rejected/rejected_customers.csv".format(BUCKET_NAME))
print("\nETL pipeline completed successfully!")
