import logging
import os
from datetime import datetime

# Directory for logs
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Log file name with timestamp
log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M.log")

# Full path for log in the logs directory
log_file_path = os.path.join(logs_dir, log_filename)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)
if __name__ == "__main__":
    logging.info("Logger initialized")