import logging
from logging import StreamHandler,FileHandler
from logging import Formatter

# 创建日志记录器
logger = logging.getLogger(name="spider")
logger.setLevel(logging.DEBUG)

# 创建日志处理器
handler = StreamHandler()
handler.setLevel(logging.INFO)

# 创建日志格式化对象
formatter = Formatter(fmt="[ %(asctime)s of %(name)s - %(levelname)s] %(message)s",datefmt='%Y-%m-%d %H:%M:%S')

# 设置处理器的日期格式化
handler.setFormatter(formatter)

# 添加记录器的处理器
logger.addHandler(handler)

fileHandler = FileHandler('log.log',encoding='utf8')

fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger.info("nihaoa")
logger.debug("debug")