class TrieNode:
    def __init__(self, val=None, end=False):
        self.val = val
        self.children = dict()  # character:TrieNode
        self.end = end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string, val=None):
        node = self.root
        idx_not_found = None
        for i, c in enumerate(string):
            if c in node.children:
                node = node.children[c]
            else:
                idx_not_found = i
                break
        if idx_not_found is not None:
            for i in range(idx_not_found, len(string)):
                c = string[i]
                node.children[c] = TrieNode()
                node = node.children[c]
                if i == len(string)-1:
                    node.end = True
        node.val = val

    def search(self, string):
        node = self.root
        for c in string:
            if c in node.children:
                node = node.children[c]
            else:
                return False, None
        return node.end, node.val

    def exist(self, string):
        node = self.root
        for c in string:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.end




