import logging
from logging import LogRecord
import os
import time

def setup_logger(path: str = "./logs/example.log", location: str = None):
    """ setup logger with logging package all log information will stored
    in *.log files format date for logfile or filename """

    # logger basic setup
    logging.basicConfig(filename=path, encoding='utf-8',
                        level=logging.DEBUG,
                        format=f'{location}: %(levelname)s: %(message)s: %(asctime)s',
                        datefmt="%m/%d/%Y %I:%M:%S %p")
    return logging

if __name__ == "__main__":
    logger = setup_logger(location="mylogger")
    logger.getLogger(__name__)
    logger.log(logger.INFO, "-- INFO LOGGER --")
    logger.log(logger.DEBUG, "-- DEBUG LOGGER --")
    logger.log(logger.WARN, "-- WARN LOGGER --")
    logger.log(logger.CRITICAL, " -- CRITICAL LOGGER --")