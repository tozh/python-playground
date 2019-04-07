from Buffer import Buffer
from Handler import Handler


class Appender(object):
    def __init__(self, target_dir, task, handler_type=Handler.FILE_WRITER, buffer_size=128):
        self.task = task
        self.buffer_size = buffer_size
        self.handler = Handler(target_dir, handler_type)
        self.buffers = {}

    def __add_buffer(self, log_item):
        buf = Buffer(log_item, self.handler, maxsize=self.buffer_size)
        if log_item.channel not in self.buffers:
            self.buffers[log_item.channel] = {log_item.level: buf}
        else:
            if log_item.level not in self.buffers[log_item.channel]:
                self.buffers[log_item.channel][log_item.level] = buf
        return buf

    def __get_buffer(self, log_item):
        return self.buffers.get(log_item.channel, {}).get(log_item.level, None)

    def append(self, log_item):
        buf = self.__get_buffer(log_item)
        if not buf:
            buf = self.__add_buffer(log_item)
        buf.append(log_item)
