from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        d = defaultdict(list)
        count = 0
        for w in words:
            d[w[0]].append(w[1:])
        last = 0
        for s in S:
            last = 0
            l = []
            for w in d[s]:
                if w:
                    w0 = w[0]
                    w1 = w[1:]
                    if w1 is '' :
                        last += 1
                    if w0 == s:
                        l.append(w1)
                    else:
                        d[w0].append(w1)
                else:
                    d[w].append('')

            d[s] = l
        return len(d[''])+last


