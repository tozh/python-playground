import sys
import re
s = '这是一个测试。haha；呵呵： test my word count, I want to know. '

def count_word(s):
    zh_regex = re.compile(r'[\u4e00-\u9fa5|，。！？…（）：；]+')
    zh_count = 0
    en_count = 0
    en_list = []
    for w in s:
        if zh_regex.match(w):
            zh_count += 1
            en_list.append(' ')
        else:
            en_list.append(w)
    blank_regex = re.compile(r'\s+')
    words = blank_regex.split(''.join(en_list))
    for w in words:
        if w:
            en_count += 1

    return en_count + zh_count

print(count_word(s))