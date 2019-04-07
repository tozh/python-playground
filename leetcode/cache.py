from collections import deque

'''
Cache with size = s
Least Frequently Used Cache
get/put if a in the Cache: time +1
get(a) put(a) both are O(1)
'''


class KeyNode:
    def __init__(self, key, val, freq = 1):
        self.key = key
        self.val = val
        self.freq = freq
        self.pre = None
        self.next = None


class FreqNode:
    def __init__(self, freq, pre, next):
        self.freq = freq
        self.pre = pre
        self.next= next
        self.first = None
        self.last = None


class LFUCache:
    def __init__(self, size):
        self.size = size
        self.key_nodes = {}
        self.freq_nodes = {}
        self.min_freq = 0
        self.count = 0
        self.head = FreqNode(0, None, None)

    def get(self, key):
        if key in self.key_nodes:
            self.update_freq(key)
            return self.key_nodes[key].val
        else:
            return None

    def put(self, key, val):
        if key in self.key_nodes:
            self.key_nodes[key].val = val
            self.update_freq(key)
        else:
            if self.count == self.size():
                min_f = self.freq_nodes[self.min_freq]
                if min_f.first == min_f.last:
                    min_f.next.pre = self.head
                    self.head.next = min_f.next
                else:
                    min_f.first.next.pre = min_f.first.pre
                    min_f.first = min_f.first.next

            self.min_freq = 1

            if 1 in self.freq_nodes:
                freq_node = self.freq_nodes[1]
                new_node = KeyNode(key, val)
                freq_node.first.next.pre = new_node
                new_node.next = freq_node.first.next
                freq_node.first = new_node.next
            else:
                freq_node = FreqNode(1, self.head, self.head.next)
                self.head.next.pre = freq_node
                self.head.next = freq_node
                new_node = KeyNode(key, val)
                freq_node.first = new_node
                freq_node.last = new_node
                self.min_freq = 1

    def update_freq(self, key):
        key_node = self.key_nodes[key]
        freq_node = self.freq_nodes[key_node.freq]

        freq = key_node.freq
        key_node.freq += 1
        add_one_freq = key_node.freq

        if add_one_freq in self.freq_nodes:
            next_freq_node = self.freq_nodes[add_one_freq]

            if freq_node.first == key_node and freq_node.last == key_node:
                freq_node.pre.next = next_freq_node
                next_freq_node.pre = freq_node.pre
                self.freq_nodes.pop(freq)
            else:
                if key_node.pre:
                    key_node.pre.next = key_node.next

                if key_node.next:
                    key_node.next.pre = key_node.pre

                if freq_node.first == key_node:
                    freq_node.first = key_node.pre

                if freq_node.last == key_node:
                    freq_node.last = key_node.next

            next_freq_node.last.next = key_node
            key_node.pre = next_freq_node.last
            key_node.next = None
            next_freq_node.last = key_node

        else:
            if freq_node.first == key_node and freq_node.last == key_node:
                freq_node.freq += 1
                self.freq_nodes.pop(freq)
                self.freq_nodes[add_one_freq] = freq_node
            else:
                next_freq_node = FreqNode(add_one_freq, freq_node, freq_node.next)
                if freq_node.next:
                    freq_node.next.pre = next_freq_node
                freq_node.next = next_freq_node



                if key_node.pre:
                    key_node.pre.next = key_node.next

                if key_node.next:
                    key_node.next.pre = key_node.pre

                if freq_node.first == key_node:
                    freq_node.first = key_node.pre

                if freq_node.last == key_node:
                    freq_node.last = key_node.next
                key_node.next = None
                key_node.pre = None
                next_freq_node.first = key_node
                next_freq_node.last = key_node