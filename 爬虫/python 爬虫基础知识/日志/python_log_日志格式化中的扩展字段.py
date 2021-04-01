'''
日志格式化中的扩展字段
- %(扩展字段名)s
- loger.info(msg,extra)
'''

import logging
from logging import StreamHandler,FileHandler
from logging import Formatter


def init_logger():
    '''
    filename  Specifies that a FileHandler be created, using the specified
              filename, rather than a StreamHandler.
    filemode  Specifies the mode to open the file, if filename is specified
              (if filemode is unspecified, it defaults to 'a').
    format    Use the specified format string for the handler.
    datefmt   Use the specified date/time format.
    style     If a format string is specified, use this to specify the
              type of format string (possible values '%', '{', '$', for
              %-formatting, :meth:`str.format` and :class:`string.Template`
              - defaults to '%').
    level     Set the root logger level to the specified level.
    stream    Use the specified stream to initialize the StreamHandler. Note
              that this argument is incompatible with 'filename' - if both
              are present, 'stream' is ignored.
    handlers  If specified, this should be an iterable of already created
              handlers, which will be added to the root handler. Any handler
              in the list which does not have a formatter assigned will be
              assigned the formatter created in this function.
    '''
    # 配置root 记录器基本信息
    logging.basicConfig(format='<%(asctime)s> of <%(user_id)s> at %(pathname)s %(lineno)d line',datefmt='%Y-%m-%d %H:%M:%S',level=logging.INFO)

if __name__ == "__main__":
    # logger = logging.getLogger() # root
    # extra 指定扩展名的值
    init_logger()
    logging.info("hi,yby",extra={'user_id':'10091'})

    logging.warning('warning yby',extra={'user_id':"12456"})