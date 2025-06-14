import logging,os
from datetime import datetime

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)#this is the log file name

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    #This defines how each log entry will be formatted:

    # %(asctime)s: Timestamp of the log entry
    # %(lineno)d: Line number where the logging call was made
    # %(name)s: Logger name (usually the module name)
    # %(levelname)s: Logging level (INFO, ERROR, etc.)
    # %(message)s: The actual log message
    level=logging.INFO,#Sets the minimum logging level to INFO
    # Will capture INFO, WARNING, ERROR, and CRITICAL messages
    # Will not capture DEBUG messages
    
)
    
    # 
    