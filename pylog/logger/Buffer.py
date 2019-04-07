import Queue

class Buffer(object):
    def __init__(self, log_item, handler, maxsize=128, prioritized=False):
        self.task = log_item.task
        self.channel = log_item.channel
        self.level = log_item.level
        self.handler = handler
        assert maxsize >= 1
        self.maxsize = maxsize
        if prioritized:
            self.queue = Queue.PriorityQueue(maxsize=maxsize)
        else:
            self.queue = Queue.Queue(maxsize=maxsize)
        # self.append(log_item)

    def append(self, log_item):
        if log_item:
            if self.queue.qsize() + 1 >= self.maxsize:
                self.queue.put(log_item)
                self.handler.handle(self)
            else:
                self.queue.put(log_item)

    def empty(self):
        return self.queue.empty()

    def pull(self):
        return self.queue.get()

    def __del__(self):
        # finally, clear the buffer and handle
        self.handler.handle(self)
