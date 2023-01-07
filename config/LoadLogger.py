"""
This is the Logger configurations.

@autor: Byron Andrango
@since: 2023 - Jan
@version: 1.0
"""
import logging

# import own libraries
import config.LoadFileConfig as cf

from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# Logger configuration  
conf = cf.loadConfig()

file_log = conf['app']['log']['directory']

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

# Configure level and formatter and add it to handlers
file_format = logging.Formatter('%(asctime)s - [%(levelname)s] - [%(threadName)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')

# Create handlers
handler = TimedRotatingFileHandler(file_log, when='H', interval=1, backupCount=12)
handler.setFormatter(file_format)
logger.addHandler(handler)