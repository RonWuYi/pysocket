import logging

from datetime import datetime as dt

logging.basicConfig(
    filename='/home/hdc/Downloads/github/pysocket/log/{}.log'.format(str(dt.today())[:16]), level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too1')
