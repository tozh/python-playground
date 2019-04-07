# coding=utf-8
import os
import time
from Appender import Appender
from Handler import Handler

FATAL = 'FATAL'
ERROR = 'ERROR'
WARN = 'WARN'
INFO = 'INFO'
DEBUG = 'DEBUG'

LEVEL_NAME = {
    FATAL: 'FATAL',
    ERROR: 'ERROR',
    WARN: 'WARN',
    INFO: 'INFO',
    DEBUG: 'DEBUG'
}
MSG_MAX = 1 << 10
FILE_PATH_MAX = 1 << 6


class LogItem(object):
    def __init__(self, task, channel, level, msg, str_extra='', int_extra=0):
        self.task = task
        self.channel = channel
        self.level = level
        self.msg = msg
        self.str_extra = str(str_extra)
        self.int_extra = int(int_extra)
        # self.id = self.__generate_log_id()
        self.datetime = self.__now_datetime()

    # def __cmp__(self, other):
    #     if self.level == other.level:
    #         return self.id.__cmp__(other.id)
    #     else:
    #         return self.level.__cmp__(other.level)

    def __now_datetime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def __generate_log_id(self):
        log_hash = hash(self.task+self.channel+str(self.level)) % FILE_PATH_MAX
        msg_hash = hash(self.msg) % MSG_MAX
        nanosec = int(round(time.time() * 1000000))
        return (nanosec << 22) + (log_hash << 6) + msg_hash

    # def __str__(self):
    #     string = '{level}: Id: {id}, Time: {datetime}, Task: {task}, Channel: {channel},' \
    #              'Msg: {msg}, StrExt: {str_extra}, IntExt: {int_extra}\n'\
    #         .format(level=self.level, id=self.id, datetime=self.datetime,
    #                 task=self.task, channel=self.channel, msg=self.msg,
    #                 str_extra=self.str_extra, int_extra=self.int_extra)
    #     return string
    def __str__(self):
        string = '{level}: Time: {datetime}, Task: {task}, Channel: {channel},' \
                 'Msg: {msg}, StrExt: {str_extra}, IntExt: {int_extra}\n'\
            .format(level=self.level, datetime=self.datetime,
                    task=self.task, channel=self.channel, msg=self.msg,
                    str_extra=self.str_extra, int_extra=self.int_extra)
        return string


class Logger(object):
    def __init__(self, target_dir, task, handler_type=Handler.FILE_WRITER, buffer_size=64):
        self.task = task
        self.appender = Appender(target_dir, task, handler_type, buffer_size)

    def log(self, channel, level, msg, str_extra='', int_extra=0):
        log_item = LogItem(self.task, channel=channel, level=level, msg=msg, str_extra=str_extra, int_extra=int_extra)
        self.appender.append(log_item)

    def fatal(self, channel, msg, str_extra='', int_extra=0):
        self.log(channel=channel, level=FATAL, msg=msg, str_extra=str_extra, int_extra=int_extra)

    def error(self, channel, msg, str_extra='', int_extra=0):
        self.log(channel=channel, level=ERROR, msg=msg, str_extra=str_extra, int_extra=int_extra)

    def warn(self, channel, msg, str_extra='', int_extra=0):
        self.log(channel=channel, level=WARN, msg=msg, str_extra=str_extra, int_extra=int_extra)

    def info(self, channel, msg, str_extra='', int_extra=0):
        self.log(channel=channel, level=INFO, msg=msg, str_extra=str_extra, int_extra=int_extra)

    def debug(self, channel, msg, str_extra='', int_extra=0):
        self.log(channel=channel, level=DEBUG, msg=msg, str_extra=str_extra, int_extra=int_extra)