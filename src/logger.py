import os
import logging
from datetime import datetime

log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(log_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(log_path,log_file)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s-%(message)s",
    level=logging.INFO
)

if __name__=="__main__":
    logging.info("LOGGING HAS STARTED")