# class EmptyStateError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return repr(self.msg)
#
# try:
#     for i in range(0, 3):
#         print(3)
#         raise EmptyStateError('EmptyState happens!')
#         print(1)
# except EmptyStateError as e:
#     print(e)

# import re
#
# with open("cookies", "r") as c:
#     string = c.read()
#     c.close()
# print(string)
#
# pattern = re.compile(r'z_c0=.*\\""')
# search = pattern.search(string)
# print(search.group(0).split('\\\"')[1])

import threading
import time
import re

str = '5+4-3+3'
print(re.split(r'[+-]', str))


