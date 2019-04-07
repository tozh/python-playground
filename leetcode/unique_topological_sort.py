from collections import deque


class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        indegree, outedges = self.buildGrpah(org, seqs)
        deck = deque()
        for n, degree in indegree:
            if degree == 0:
                deck.append(n)
        if len(deck) != 1:
            return False

        while len(deck) != 0:
            n = deck.popleft()
            append_count = 0
            for m in outedges[n]:
                indegree[m] -= 1
                if indegree[m] == 0:
                    append_count += 1
                    deck.append(m)
            if append_count != 0:
                return False

        for n, degree in indgree:
            if degree != 0:
                return False

        return True

    def buildGrpah(self, org, seqs):
        indegree = {i: 0 for i in org}
        outedges = {i: [] for i in org}

        for seq in seqs:
            for i in range(1, len(seq)):
                s1 = seq[i - 1]
                s2 = seq[i]
                indegree[s2] += 1
                outedges[s1].append(s2)

        return indegree, outedges

