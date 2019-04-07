import os

class FileWriter(object):
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.log_dir = os.path.join(self.target_dir, 'log/')
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def handle(self, buf):
        task = buf.task
        channel = buf.channel
        level = buf.level
        log_file = os.path.join(self.log_dir, task + '.' + channel + '.' + level + '.log')
        with open(log_file, 'a+') as f:
            while not buf.empty():
                f.write(str(buf.pull()))
            f.close()


class Handler(object):
    FILE_WRITER = 1

    HANDLER_TYPE = {
        FILE_WRITER: FileWriter
    }

    def __init__(self, target_dir, handler_type=FILE_WRITER):
        self.handler_type = handler_type
        self.handler = Handler.HANDLER_TYPE[self.handler_type](target_dir)

    def handle(self, buf):
        self.handler.handle(buf)


