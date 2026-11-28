
from pathlib import Path

from src.extract import extract_sales
from src.validate import validate_sales
from src.transform import transform_sales
from src.database import get_dimension_lookups
from src.load import load_sales
from src.reject_handler import save_rejected_records
from src.logger import get_logger


def main():
    """Run the complete e-commerce sales ETL pipeline."""

    logger = get_logger()

    logger.info("=" * 50)
    logger.info("E-COMMERCE SALES ETL PIPELINE STARTED")
    logger.info("=" * 50)

    try:
        # 1. Extract
        project_dir = Path(__file__).resolve().parent.parent
        file_path = project_dir / "data" / "new_sales.csv"

        logger.info("Starting data extraction.")

        records = extract_sales(file_path)

        logger.info("Extraction completed: %s records.", len(records))

        # 2. Validate
        logger.info("Starting data validation.")

        valid_records, rejected_records = validate_sales(records)

        logger.info(
            "Validation completed. Valid: %s, Rejected: %s",
            len(valid_records),
            len(rejected_records)
        )

        # 3. Save rejected records
        save_rejected_records(rejected_records)

        if rejected_records:
            logger.warning(
                "%s records were rejected.",
                len(rejected_records)
            )

        # 4. Stop if no valid records exist
        if not valid_records:
            logger.warning("No valid records available for processing.")
            return

        # 5. Retrieve dimension lookups
        logger.info("Retrieving customer and product dimension lookups.")

        customer_lookup, product_lookup = get_dimension_lookups()

        # 6. Transform
        logger.info("Starting data transformation.")

        transformed_records = transform_sales(
            valid_records,
            customer_lookup,
            product_lookup
        )

        logger.info(
            "Transformation completed: %s records.",
            len(transformed_records)
        )

        # 7. Load
        logger.info("Starting PostgreSQL data loading.")

        load_sales(transformed_records)

        # 8. Pipeline summary
        logger.info("=" * 50)
        logger.info("ETL PIPELINE SUMMARY")
        logger.info("Records extracted: %s", len(records))
        logger.info("Valid records: %s", len(valid_records))
        logger.info("Rejected records: %s", len(rejected_records))
        logger.info(
            "Records sent for loading: %s",
            len(transformed_records)
        )
        logger.info("ETL PIPELINE COMPLETED SUCCESSFULLY")
        logger.info("=" * 50)

    except Exception:
        logger.exception("ETL PIPELINE FAILED.")
        raise


if __name__ == "__main__":
    main()
