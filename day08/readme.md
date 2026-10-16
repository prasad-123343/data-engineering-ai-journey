# Day 8 — Order Validation Pipeline

## Project Overview
A Python project that validates incoming order records and separates valid orders from rejected orders.

## Problem Statement
Order data may contain missing customer names, negative prices, invalid quantities, or invalid order IDs. These records must be identified before downstream processing.

## Technologies
- Python
- Git and GitHub

## Validation Rules
1. Customer name must not be empty or whitespace.
2. Price must not be negative.
3. Quantity must be greater than zero.
4. Order ID must be greater than zero.

## Pipeline Design
1. Receive order records.
2. Validate each order using `validate_order()`.
3. Use `process_orders()` to separate valid and rejected records.
4. Record the rejection reason for each invalid order.
5. Display the final counts.

## Current Results
- Total orders tested: 5
- Valid orders: 1
- Rejected orders: 4

## Limitations
- Input is currently provided directly in Python.
- Records with missing fields or unexpected data types are not yet handled safely.
- Results are displayed in the terminal rather than stored in a database.

## Future Improvements
- Read orders from JSON or a REST API.
- Add automated tests.
- Add structured logging.
- Store validated records in PostgreSQL.
