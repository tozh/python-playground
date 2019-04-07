# class Solution:
#     def alienOrder(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         if len(words) < 2:
#             return ""
#         ok, self.visit, self.out_edges, self.in_edges = self.buildGraph(words)
#         if not ok:
#             return ""
#         self.result = []
#
#         for node, out_edges in self.out_edges.items():
#             if not out_edges:
#                 ok = self.dfs(node)
#                 if not ok:
#                     return ""
#
#         return "".join(self.result)
#
#     def dfs(self, node):
#         if self.visit[node] == 1:
#             return False
#         if self.visit[node] == 2:
#             print(node)
#             return True
#
#         self.visit[node] = 1
#         for m in self.in_edges[node]:
#             if not self.dfs(m):
#                 return False
#         self.visit[node] = 2
#         self.result.append(node)
#         return True
#
#     def buildGraph(self, words):
#         letters = dict()
#         out_edges = dict()
#         in_edges = dict()
#         for i in range(1, len(words)):
#             w1 = words[i - 1]
#             w2 = words[i]
#             j = 0
#             order_found = False
#             while j < len(w1) and j < len(w2):
#                 if w1[j] not in letters:
#                     letters[w1[j]] = 0
#                     out_edges[w1[j]] = []
#                     in_edges[w1[j]] = []
#                 if w2[j] not in letters:
#                     letters[w2[j]] = 0
#                     out_edges[w2[j]] = []
#                     in_edges[w2[j]] = []
#                 if not order_found:
#                     if w1[j] != w2[j]:
#                         out_edges[w1[j]].append(w2[j])
#                         in_edges[w2[j]].append(w1[j])
#                         order_found = True
#                 j += 1
#             if not order_found and j == len(w2) and j != len(w1):
#                 return False, None, None, None
#             if j != len(w1):
#                 while j < len(w1):
#                     if w1[j] not in letters:
#                         letters[w1[j]] = 0
#                         out_edges[w1[j]] = []
#                         in_edges[w1[j]] = []
#                     j += 1
#             elif j != len(w2):
#                 while j < len(w2):
#                     if w2[j] not in letters:
#                         letters[w2[j]] = 0
#                         out_edges[w2[j]] = []
#                         in_edges[w2[j]] = []
#                     j += 1
#         print(letters)
#         print(out_edges)
#         print(in_edges)
#         return True, letters, out_edges, in_edges
#
from collections import deque
class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""
        if len(words) == 1:
            return words[0]
        ok, self.in_degree, self.out_edges = self.buildGraph(words)
        if not ok:
            return ""
        #
        self.result = []
        self.dq = deque()

        for n, degree in self.in_degree.items():
            if degree == 0:
                self.dq.append(n)

        while len(self.dq) != 0:
            n = self.dq.popleft()
            for m in self.out_edges[n]:
                self.in_degree[m] -= 1
                if self.in_degree[m] == 0:
                    self.dq.append(m)
            self.result.append(n)
        for n, degree in self.in_degree.items():
            if degree != 0:
                return ""

        return "".join(self.result)



    def buildGraph(self, words):
        in_degree = dict()
        out_edges = dict()
        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            j = 0
            order_found = False
            while j < len(w1) or j < len(w2):
                if not order_found and j == len(w2) and j != len(w1):
                    return False, None, None
                if j < len(w1) and w1[j] not in in_degree:
                    in_degree[w1[j]] = 0
                    out_edges[w1[j]] = []
                if j < len(w2) and w2[j] not in in_degree:
                    in_degree[w2[j]] = 0
                    out_edges[w2[j]] = []
                if not order_found:
                    if j < len(w1) and j < len(w2) and w1[j] != w2[j]:
                        in_degree[w2[j]] += 1
                        out_edges[w1[j]].append(w2[j])
                        order_found = True
                j += 1
        print(in_degree, out_edges)
        return True, in_degree, out_edges
s = Solution()
A = ["abc", "ab", "a"]
# A = ["bsusz","rhn","gfbrwec","kuw","qvpxbexnhx","gnp","laxutz","qzxccww"]
print(s.alienOrder(A))
