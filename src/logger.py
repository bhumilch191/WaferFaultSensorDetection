import logging
import os
from datetime import datetime

Log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
Logs_path = os.path.join(os.getcwd(),"logs",Log_file)

os.makedirs(Logs_path,Log_file)

Log_file_path = os.path.join(Logs_path,Log_file)

logging.basicConfig(
    filename=Log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)