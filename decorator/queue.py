import threading
import random

class Queue(object):
    def __init__(self, cap):
        self.q = [0] * cap
        self.cap = cap
        self.next_poll = 0
        self.next_put = 0
        # self.empty = threading.Semaphore(self.cap)
        # self.occupied = threading.Semaphore(0)

    def put(self, item):
        self.q[self.next_put] = item
        self.next_put = (self.next_put + 1) % self.cap

    def poll(self):
        item = self.q[self.next_poll]
        self.next_poll = (self.next_poll + 1) % self.cap
        return item


# class Queue(object):
#     def __init__(self, cap):
#         self.q = [0] * cap
#         self.cap = cap
#         self.next_poll = 0
#         self.next_put = 0
#         self.empty = threading.Semaphore(self.cap)
#         self.occupied = threading.Semaphore(0)
#
#
#     def put(self, item):
#         self.empty.acquire()
#         try:
#             self.q[self.next_put] = item
#             self.next_put = (self.next_put + 1) % self.cap
#         finally:
#             self.occupied.release()
#
#     def poll(self):
#         self.occupied.acquire()
#         try:
#             item = self.q[self.next_poll]
#             self.next_poll = (self.next_poll + 1) % self.cap
#             return item
#         finally:
#             self.empty.release()


class Id(object):
    def __init__(self):
        self.id = -1
        self.lock = threading.Lock()

    def __iter__(self):
        return self

    def __next__(self):
        # self.lock.acquire()
        # try:
        self.id += 1
        return self.id
        # finally:
        #     self.lock.release()

# class Test(object):
#     def __init__(self, time, thr_num):
#         self.q = Queue(time * thr_num)
#         self.thr_num = thr_num
#         self.time = time
#         self.threads = []
#         self.id_generator = Id()
#         self.q2 = Queue(time * thr_num)
#
#
#     def put(self):
#         for _ in range(self.time):
#             self.q.put(next(self.id_generator))
#
#     def poll(self):
#         for _ in range(self.time):
#             self.q2.put(self.q.poll())
#
#     def run(self):
#         for i in range(self.thr_num):
#             thr_put = threading.Thread(target=self.put)
#             thr_poll = threading.Thread(target=self.poll)
#             self.threads.append(thr_put)
#             self.threads.append(thr_poll)
#         for thr in self.threads:
#             thr.start()
#         for thr in self.threads:
#             thr.join()
#
#         for i in range(self.time * self.thr_num):
#             print(self.q2.poll())
class Test(object):
    def __init__(self, time, thr_num):
        self.q = Queue(time * thr_num)
        self.thr_num = thr_num
        self.time = time
        self.threads = []
        self.id_generator = Id()
        self.q2 = Queue(time * thr_num)
        self.id = 0

    def put(self):
        for _ in range(self.time):
            self.q.put(self.id+1)
            self.id+=1

    def poll(self):
        for _ in range(self.time):
            self.q2.put(self.q.poll())

    def run(self):
        for i in range(self.thr_num):
            thr_put = threading.Thread(target=self.put)
            thr_poll = threading.Thread(target=self.poll)
            self.threads.append(thr_put)
            self.threads.append(thr_poll)
        random.shuffle(self.threads)
        for thr in self.threads[::-1]:
            thr.start()
        for thr in self.threads:
            thr.join()

        for i in range(self.time * self.thr_num):
            print(self.q2.poll())

test = Test(5, 10)
test.run()
