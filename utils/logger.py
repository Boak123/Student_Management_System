
import logging
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Log directory
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Log file
LOG_FILE = LOG_DIR / "app.log"

# Configure logger
logging.basicConfig(
    level=logging.DEBUG,
    format=(
        "%(asctime)s - %(name)s - "
        "%(levelname)s - %(message)s"
    ),
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("student_management")


logger.warning("Invalid student data supplied.")
logger.warning("Duplicate registration attempted.")
logger.warning("Maximum student capacity reached.")
logger.info("Student registered successfully.")