import logging
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = PROJECT_DIR / "scripts"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def run_script(script_name):
    script_path = SCRIPTS_DIR / script_name

    logger.info("Starting %s", script_name)

    subprocess.run(
        [sys.executable, str(script_path)],
        check=True,
        cwd=PROJECT_DIR
    )

    logger.info("Completed %s", script_name)


def main():
    logger.info("Customer ETL pipeline started")

    try:
        run_script("create_staging.py")
        run_script("data_quality.py")
        run_script("query_customers.py")
        run_script("log_analyzer.py")

        logger.info("Customer ETL pipeline completed successfully")

    except subprocess.CalledProcessError:
        logger.exception("A pipeline script failed")
        raise


if __name__ == "__main__":
    main()
