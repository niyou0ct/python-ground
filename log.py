import logging.config

logging.config.fileConfig('logconf.ini')
logger = logging.getLogger('sample')
logger.error('Error occured')