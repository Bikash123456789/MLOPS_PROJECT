from src.logger import logging
from src.exception import CustomException
import sys

try:
    a = 1 / 0
except Exception as e:
    logging.info("Divided by Zero Exception")
    raise CustomException(e, sys)
