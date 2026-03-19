import logging
from logging.handlers import RotatingFileHandler
from Core.settings import DIR_LOGGER,MAX_MB_ROTATING_LOGS

MB = 1024 * 1024


def get_logger(name):
    
    handler = RotatingFileHandler(filename=f'{DIR_LOGGER}/app.log',maxBytes= MAX_MB_ROTATING_LOGS * MB, backupCount=5)
    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(format)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
