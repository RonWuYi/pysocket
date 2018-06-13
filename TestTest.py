import logging
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# #formatter = logging.Formatter('%(asctimes)s')
# foratter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  %(message)s')
# ch.setFormatter(foratter)
#
# logger.addHandler(ch)

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
#                                                                                                                       'logger.critical('critical message')'