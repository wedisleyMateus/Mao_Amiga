import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = RotatingFileHandler("logs/app.log", maxBytes=5_000_000, backupCount=3)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)