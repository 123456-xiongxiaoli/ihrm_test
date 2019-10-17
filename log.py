#导包
import logging
from logging import handlers

import app


def print_Log():
    #创建日志器
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    #创建处理器
    #创建输出到控制台的处理器
    ls=logging.StreamHandler()
    lf=logging.handlers.TimedRotatingFileHandler(app.PATH+"./b.log",when="H",interval=2,backupCount=2)

    #定义格式化
    fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter=logging.Formatter(fmt)
    #添加格式化到处理器
    ls.setFormatter(fmt=formatter)
    lf.setFormatter(fmt=formatter)

    #添加处理器到日志器
    logger.addHandler(ls)
    logger.addHandler(lf)


