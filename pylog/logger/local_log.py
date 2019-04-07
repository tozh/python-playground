# coding=utf-8
import os
import time


class LocalLog(object):
    def __init__(self, task, path, dir, file):
        self.task = task
        self.path = path
        self.file = file
        self.info_file = open(os.path.join(path, dir, "{0}_{1}_info.log".format(self.task, self.file)), 'a+')
        self.warning_file = open(os.path.join(path, dir, "{0}_{1}_warning.log".format(self.task, self.file)), 'a+')
        self.error_file = open(os.path.join(path, dir, "{0}_{1}_error.log".format(self.task, self.file)), 'a+')

    def info(self, file, line, uid, result):
        content = "INFO: Line: {0}, Time: {1}, File: {2}, Uid: {3}, Result: {4}\n".format(line, self.__now_datetime(), file, uid, result)
        self.info_file.write(content)

    def warning(self, file, line, uid, result, warning):
        content = "WARNING: Line: {0}, Time: {1}, File: {2}, Uid: {3}, " \
                  "Result: {4}, Warning: {5}\n".format(line, self.__now_datetime(), file, uid, result, warning)
        self.warning_file.write(content)

    def error(self, file, line, uid, result, err, extra):
        content = "ERROR: Line: {0}, Time: {1}, File: {2}, Uid: {3}, Result: {4}, " \
                  "ErrorType: {5}, ErrorInfo: {6}, Extra: {7}\n".format(line,
                                                                        self.__now_datetime(), file, uid, result,
                                                                        err.__str__(), err.__repr__(), extra)
        self.error_file.write(content)

    def __now_datetime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    def __del__(self):
        self.info_file.close()
        self.warning_file.close()
        self.error_file.close()

if __name__ == '__main__':
    logger = LocalLog('send_notice', "/Users/zhaotong", 'diyigefile')
    for _ in range(10):
        logger.info('try', 123456789, 1)
        logger.warning('try', 123456789, 1, 'yashileni')
        logger.error('try', 123456789, 1, Exception())