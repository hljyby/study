import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
fomatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

handler.setFormatter(fomatter)
logger.addHandler(handler)

logger.info('start print log')
logger.debug('start print debug')
logger.warning('start print warning')
logger.info('finish')
