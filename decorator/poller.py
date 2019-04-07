from abc import ABCMeta, abstractmethod
import os
import time

class Poller(metaclass=ABCMeta):
    @abstractmethod
    def init_poll(self):
        pass

    # @abstractmethod
    # def add(self, item):
    #     pass
    #
    # @abstractmethod
    # def remove(self, item):
    #     pass

    @abstractmethod
    def run(self, interval, max_loop=None):
        pass

    def ready(self, item):
        pass

    def dowork(self, item):
        pass


class FilePoller(Poller):
    def __init__(self, directory):
        self.dir = directory
        self.poll_list = []
        self.poll_initialized = False

    def init_poll(self):
        self.poll_list = os.listdir(self.dir)
        self.poll_initialized = True

    def ready(self, item):
        if os.path.isfile(os.path.join(self.dir, item)):
            return True
        return False

    def dowork(self, item):
        if self.ready(item):
            print(item)

    def run(self, interval, max_loop=None):
        if not self.poll_initialized:
            raise Exception("not initialized poller")

        def one_loop():
            for item in self.poll_list:
                if self.ready(item):
                    self.dowork(item)
                time.sleep(interval)

        if max_loop is None:
            max_loop = float("inf")
        count = 0
        while count < max_loop:
            print("-------->loop {count}".format(count=count))
            one_loop()
            print()
            count += 1

fp = FilePoller("/Users/zhaotong/Gdrive")
fp.init_poll()
fp.run(0.1, 2)

