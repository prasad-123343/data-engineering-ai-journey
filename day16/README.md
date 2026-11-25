# Day 16 — AWS S3 Cloud ETL Pipeline

## 1. Project Overview

This project demonstrates a beginner-friendly cloud-based ETL pipeline using Python, AWS S3, Boto3, and AWS CLI.

The pipeline reads customer data from an AWS S3 bucket, validates the records, separates valid and invalid records, and uploads the results back to S3.

The project also includes a local ETL simulation using Python and CSV files.

## 2. Technologies Used

- Python 3.13
- AWS S3
- AWS CLI
- Boto3 (AWS SDK for Python)
- CSV
- Git and GitHub

## 3. Project Structure

```text
day16/
├── aws_s3/
│   ├── __init__.py
│   └── s3_connection.py
├── data_lake/
│   ├── raw/
│   │   └── customers.csv
│   └── processed/
│       ├── customers.csv
│       └── rejected_customers.csv
├── organize_data.py
└── requirements.txt
```

## 4. AWS S3 Bucket Structure

**Bucket:** `prasad-de-apprenticeship-2026`

**AWS Region:** `ap-southeast-2` (Sydney)

```text
prasad-de-apprenticeship-2026/
├── raw/
│   └── customers.csv
├── processed/
│   └── customers.csv
├── rejected/
│   └── rejected_customers.csv
└── curated/
```

The prefixes represent different data lake stages:

- `raw/`: Original source data.
- `processed/`: Records that passed validation.
- `rejected/`: Records that failed validation.
- `curated/`: Reserved for future refined datasets.

## 5. ETL Workflow

### Extract

- Connect to AWS S3 using Boto3.
- Read `raw/customers.csv` using `get_object()`.
- Parse CSV records using Python's `csv.DictReader`.

### Transform

- Check that `customer_id`, `name`, and `city` are not empty.
- Store valid records separately from rejected records.

### Load

- Convert Python records into CSV data.
- Upload valid records to `processed/customers.csv`.
- Upload rejected records to `rejected/rejected_customers.csv`.
- Use Boto3's `put_object()` method.

## 6. Data Quality Results

The sample input contains five customer records.

| Metric | Result |
|---|---:|
| Total records | 5 |
| Valid records | 4 |
| Rejected records | 1 |
| Validation success rate | 80% |

Customer 4 was rejected because its name field was empty.

## 7. Setup Instructions

### Prerequisites

- Python installed.
- AWS CLI installed.
- An AWS account with access to the required S3 bucket.
- Appropriate IAM permissions.

### Install dependencies

From the repository root:

```powershell
python -m pip install -r day16/requirements.txt
```

### Authenticate with AWS

```powershell
aws login --region ap-southeast-2
```

Verify your AWS identity:

```powershell
aws sts get-caller-identity --region ap-southeast-2
```

### Run the cloud ETL pipeline

```powershell
python day16/aws_s3/s3_connection.py
```

## 8. Verify S3 Outputs

Check the processed records:

```powershell
aws s3 ls s3://prasad-de-apprenticeship-2026/processed/ --region ap-southeast-2
```

Check the rejected records:

```powershell
aws s3 ls s3://prasad-de-apprenticeship-2026/rejected/ --region ap-southeast-2
```

Read the processed CSV:

```powershell
aws s3 cp s3://prasad-de-apprenticeship-2026/processed/customers.csv - --region ap-southeast-2
```

## 9. Security and Cost Considerations

- The S3 bucket has Block Public Access enabled.
- The bucket uses server-side encryption with S3-managed keys (SSE-S3).
- AWS CLI login provides temporary credentials.
- Credentials are not hardcoded in the Python source.
- The sample data is synthetic.
- AWS Free plan usage and budget alerts should be monitored.
- S3 requests and storage may incur charges depending on usage and account terms.

## 10. Current Limitations

- Validation currently checks only whether required fields are empty.
- The pipeline does not yet include duplicate detection.
- There is no automated retry mechanism.
- There is no workflow scheduler.
- The pipeline is designed for a small CSV dataset, not large-scale ingestion.
- The same S3 output keys are overwritten when the script runs again.

## 11. Future Improvements

- Add duplicate detection and stronger schema validation.
- Add structured logging and exception handling.
- Implement pagination for large S3 object listings.
- Add automated tests.
- Introduce AWS Lambda or Apache Airflow for orchestration.
- Add monitoring and data quality reporting.
- Explore Parquet format and partitioned data storage.

## 12. Learning Outcomes

Through this project, I practised:

- AWS cloud fundamentals.
- S3 buckets, objects, and prefixes.
- IAM and temporary AWS credentials.
- AWS CLI operations.
- Python integration with AWS using Boto3.
- Extracting CSV data from cloud storage.
- Data validation and rejection handling.
- Uploading processed data to S3.
- Git and GitHub project version control.

---

**Project:** Data Engineering Apprenticeship — Day 16  
**Focus:** AWS Cloud Fundamentals and S3-based ETL