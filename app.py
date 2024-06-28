from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException

logging.info("Welcome to the custom log")

try:
    a= 4/"6"
except Exception as e:
    raise AppException(e, sys)
    