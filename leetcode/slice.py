class TrieNode:
    def __init__(self, count=0, data=None, end=False):
        self.children = dict()
        self.data = data
        self.end = end
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.data.__lt__(other.data)
        else:
            return other.count.__lt__(self.count)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, string, count):
        node = self.root
        for c in string:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.data = string
        node.end = True
        node.count += count


class AutocompleteSystem:

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        for s, count in zip(sentences, times):
            self.trie.add(s, count)

        self.node = self.trie.root
        self.result = []
        self.inputs = []

    def dfs(self, node):
        if node.end:
            self.result.append(node)
            return
        for c, n in node.children.items():
            self.dfs(n)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.node.end = True
            self.node.data = "".join(self.inputs)
            self.node.count += 1
            self.inputs = []
            self.node = self.trie.root
            temp = [n.data for n in self.result]
            return temp[:3]
        else:
            self.result = []
            self.inputs.append(c)
            if c in self.node.children:
                self.node = self.node.children[c]
                self.dfs(self.node)
            else:
                self.node.children[c] = TrieNode()
                self.node = self.node.children[c]

            self.result.sort()
            temp = [n.data for n in self.result]
            return temp[:3]


sentences = ["i love you", "island", "iroman", "i love leetcode"]
times = [5, 3, 2, 2]
a = AutocompleteSystem(sentences, times)
print(a)
param_1 = a.input("i")
print(param_1)
