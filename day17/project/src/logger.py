
import logging
from pathlib import Path


def get_logger():
    """Configure and return the ETL pipeline logger."""

    project_dir = Path(__file__).resolve().parent.parent
    log_directory = project_dir / "logs"

    # Create logs directory if it doesn't exist
    log_directory.mkdir(parents=True, exist_ok=True)

    log_file = log_directory / "etl_pipeline.log"

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(
                log_file,
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ],
        force=True
    )

    logger = logging.getLogger("ecommerce_etl")

    return logger
