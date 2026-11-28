# E-Commerce Sales Analytics Data Warehouse

## 1. Project Overview

This project implements a Python-based ETL pipeline that extracts e-commerce sales data from CSV files, validates and transforms the records, and loads them into a PostgreSQL dimensional data warehouse.

The project demonstrates practical data engineering concepts, including:

- ETL pipeline development
- CSV data ingestion
- Data validation and rejection handling
- Dimensional data modeling
- PostgreSQL integration using Psycopg 3
- Surrogate key lookups
- Idempotent data loading
- Transaction management
- Logging and error handling
- Secure database credential management

## 2. Business Problem

E-commerce businesses need reliable analytical data to understand sales performance, customer behavior, product performance, and revenue trends.

Raw sales data often contains inconsistent or invalid records. Loading such data directly into an analytical database can cause inaccurate reports and unreliable business decisions.

This project addresses that problem by implementing a structured ETL process that validates incoming sales records before loading them into a dimensional data warehouse.

## 3. Architecture and ETL Workflow

The pipeline follows this workflow:

**CSV Source → Extract → Validate → Reject Handling → Transform → PostgreSQL Load → Analytics**

### Pipeline stages

1. **Extract:** Reads sales records from a CSV file using Python's `csv` module.
2. **Validate:** Checks required fields, dates, quantities, and unit prices.
3. **Reject Handling:** Preserves invalid records and their validation errors in a separate CSV file.
4. **Dimension Lookup:** Retrieves customer and product surrogate keys from PostgreSQL.
5. **Transform:** Converts source identifiers into warehouse keys and prepares appropriate data types.
6. **Load:** Inserts valid sales records into PostgreSQL using parameterized SQL.
7. **Logging:** Records pipeline execution events, timestamps, and errors.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | ETL development |
| PostgreSQL | Relational database and data warehouse |
| Psycopg 3 | Python-PostgreSQL integration |
| SQL | Data modeling and analytical queries |
| CSV | Source data format |
| Git | Version control |
| GitHub | Source code management |
| VS Code | Development environment |
| Python Logging | Pipeline monitoring |

## 5. Database Schema and Dimensional Model

The project uses a dimensional data model based on a star schema.

### Dimension tables

**dim_customers**

Stores customer descriptive information.

- customer_key — Surrogate primary key
- customer_id — Source customer identifier
- customer_name — Customer name
- city — Customer location

**dim_products**

Stores product descriptive information.

- product_key — Surrogate primary key
- product_id — Source product identifier
- product_name — Product name
- category — Product category

**dim_date**

Stores calendar attributes.

- date_key — Primary key
- full_date — Calendar date
- day — Day of month
- month — Month number
- month_name — Month name
- quarter — Calendar quarter
- year — Calendar year
- day_of_week — Day name

### Fact table

**fact_sales**

Stores measurable sales transactions.

- sale_id — Automatically generated primary key
- order_id — Source order identifier
- customer_key — Foreign key to dim_customers
- product_key — Foreign key to dim_products
- sale_date — Sales transaction date
- date_key — Foreign key to dim