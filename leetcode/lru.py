class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.last = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, node):
        if self.tail:
            self.tail.next = node
            node.last = self.tail
            self.tail = node
        else:
            self.tail = node
            self.head = node
        self.len += 1

    def popleft(self):
        if not self.head:
            return
        node = self.head
        self.head = node.next
        if self.head:
            self.head.last = None
        else:
            self.tail = None
        self.len -= 1
        return node

    def print_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.key)
            node = node.next
        print(result)

    def to_tail(self, node):
        if node == self.tail:
            return
        node.next.last = node.last
        if node == self.head:
            self.head = node.next
        if node.last:
            node.last.next = node.next
        self.tail.next = node
        node.last = self.tail
        node.next = None
        self.tail = node


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.ls = LinkedList()
        self.d = dict()
        self.cap = capacity
        self.len = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            node = self.d[key]
            self.ls.to_tail(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.ls.to_tail(node)
        else:
            if self.len == self.cap:
                poped = self.ls.popleft()
                print(poped.key, poped.val)
                if poped:
                    self.len -= 1
                    self.d.pop(poped.key)
                print(self.d)
            node = Node(key, value)
            self.d[key] = node
            self.ls.append(node)
            self.len += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

ls = LinkedList()
a = Node(5, 1)
ls.append(Node(1, 1))
ls.append(Node(2, 2))
ls.append(Node(3, 2))
ls.append(Node(4, 1))
ls.append(a)
ls.print_list()
print(ls.head.key)
print(ls.tail.key)
ls.to_tail(a)
print(ls.head.key)
print(ls.tail.key)
ls.print_list()

# print(ls.popleft().key)
# print(ls.popleft().key)
# print(ls.popleft().key)
# print(ls.popleft().key)
# print(ls.popleft().key)

