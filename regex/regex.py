import re
# pattern = r'([0-9]+)([/*+-])([0-9]+)+'
# pattern = r'([0-9]+[/*+-]){1,}?'
#
# content = '23+189+183-16/254'
pattern = r'[*\-+/()]'
content = '+'
if re.match(pattern, content):
    print(1)