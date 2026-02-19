import logging
import os
from datetime import datetime

class RelativePathFormatter(logging.Formatter):
    def format(self, record):
        # Normalize path for Windows/Linux
        path = record.pathname.replace("\\", "/")

        # Trim path to start from src/
        if "/src/" in path:
            record.pathname = path.split("/src/", 1)[1]
            record.pathname = f"src/{record.pathname}"

        return super().format(record)


LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

handler = logging.FileHandler(LOG_FILE_PATH)
formatter = RelativePathFormatter(
    '[%(asctime)s] [%(pathname)s:%(lineno)d] %(levelname)s - %(message)s'
)

handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)