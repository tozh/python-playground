from Logger import Logger
import traceback

task = 'notice'
path = '/data00/users/zhaotong.zt/zt/'

logger = Logger(path, task)
try:
    logger.info('zt0', 'sent', 123456, 0)
except:
    traceback.print_stack()
