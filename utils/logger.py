from loguru import logger
import os

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger.add(
    f"{LOG_DIR}/app.log",
    rotation="1 MB",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
)

def get_logger():
    return logger