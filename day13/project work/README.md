# REST API Data Ingestion Pipeline

## 1. Project Overview

This project demonstrates an end-to-end data ingestion pipeline built using Python.

The pipeline retrieves data from an external REST API, validates the incoming records, separates valid and rejected data, stores the results in JSON files, loads valid records into a SQLite database, and performs SQL analytics.

The project uses the JSONPlaceholder API as its data source.

## 2. Project Objectives

The main objectives of this project are:

- Retrieve data from an external REST API.
- Extract records using pagination.
- Validate incoming JSON data.
- Separate valid and rejected records.
- Store processed records in JSON files.
- Load valid records into a SQLite database.
- Prevent duplicate records during database loading.
- Perform SQL queries to analyze stored data.
- Build a modular and reusable Python pipeline.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Requests | Communicate with the REST API |
| REST API | External data source |
| JSON | Data interchange and file storage |
| SQLite | Relational database |
| SQL | Data querying and analysis |
| VS Code | Code editor |
| Git | Version control |

## 4. Project Structure

```text
project work/
│
├── main_pipeline.py
│
├── ingestion/
│   ├── __init__.py
│   └── extract.py
│
├── processing/
│   ├── __init__.py
│   └── validate.py
│
├── storage/
│   ├── __init__.py
│   ├── save_json.py
│   └── load_sqlite.py
│
├── analytics/
│   ├── __init__.py
│   └── run_queries.py
│
├── output/
│   ├── valid_posts.json
│   └── rejected_posts.json
│
├── posts.db
└── README.md
```

## 5. Pipeline Workflow

The pipeline consists of five main stages.

### Stage 1: Data Extraction

- Connect to the JSONPlaceholder REST API.
- Send HTTP GET requests using Python Requests.
- Retrieve records in batches of 10 using pagination.
- Continue retrieving records until no more data is available.
- Extract 100 records successfully.

### Stage 2: Data Validation

Validate each record using the following rules:

- `userId` must be an integer.
- `id` must be an integer.
- `title` must be a non-empty string.
- `body` must be a non-empty string.

Separate records into valid and rejected categories.

### Stage 3: JSON Storage

Save the processed records into two JSON files:

- `valid_posts.json`
- `rejected_posts.json`

This preserves both valid data and records that fail validation.

### Stage 4: SQLite Database Loading

- Connect to the SQLite database.
- Create the `posts` table if it does not exist.
- Insert valid records using `executemany()`.
- Use `INSERT OR IGNORE` to prevent duplicate primary key IDs.
- Commit database changes.

### Stage 5: SQL Analytics

Execute SQL queries to:

- Count the total number of posts.
- Count posts belonging to each user.
- Retrieve posts with IDs greater than 90.

## 6. Data Validation Rules

| Field | Validation rule |
|---|---|
| userId | Integer |
| id | Integer |
| title | Non-empty string |
| body | Non-empty string |

Invalid records are stored separately along with their rejection reasons.

## 7. Database Design

Database name: `posts.db`

Table name: `posts`

| Column | Data type | Description |
|---|---|---|
| id | INTEGER PRIMARY KEY | Unique post identifier |
| userId | INTEGER | User identifier |
| title | TEXT | Post title |
| body | TEXT | Post content |

The `id` column acts as the primary key to ensure unique post IDs.

## 8. SQL Analytics

### Query 1: Count total posts

```sql
SELECT COUNT(*)
FROM posts;
```

### Query 2: Count posts per user

```sql
SELECT userId, COUNT(*)
FROM posts
GROUP BY userId
ORDER BY userId;
```

### Query 3: Retrieve posts with IDs greater than 90

```sql
SELECT id, title
FROM posts
WHERE id > 90
ORDER BY id;
```

## 9. How to Run the Project

### Step 1: Install the Requests library

```powershell
python -m pip install requests
```

### Step 2: Navigate to the project folder

```powershell
cd "day13\project work"
```

### Step 3: Execute the complete pipeline

```powershell
python main_pipeline.py
```

## 10. Project Results

The pipeline was executed successfully.

| Metric | Result |
|---|---:|
| Total records extracted | 100 |
| Valid records | 100 |
| Rejected records | 0 |
| Records loaded into SQLite | 100 |
| Records after second pipeline run | 100 |

The pipeline was executed twice. The database still contained 100 records after the second execution, demonstrating duplicate prevention for the loaded records.

## 11. Key Data Engineering Concepts Learned

- REST API data ingestion
- HTTP GET requests
- Pagination
- JSON processing
- Data validation
- Data quality
- Rejected record handling
- Modular programming
- Python file handling
- SQLite database operations
- SQL queries and aggregation
- Primary keys
- Duplicate prevention
- Idempotency
- ETL workflow
- End-to-end pipeline development

## Conclusion

This project demonstrates how Python can be used to build a modular data ingestion pipeline that retrieves external data, validates it, stores it in JSON and SQLite, and performs SQL analytics.

It provides practical experience with fundamental data engineering concepts and establishes a foundation for building more advanced data pipelines.