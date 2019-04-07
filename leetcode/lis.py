class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq = []
        for n in nums:
            idx = self.binarySearch(seq, n)
            if idx == len(seq):
                seq.append(n)
            else:
                seq[idx] = n
        return len(seq)

    def binarySearch(self, seq, target):
        l = 0
        r = len(seq)
        while l < r:
            m = (l + r) >> 1
            if seq[m] >= target:
                r = m
            else:
                l = m + 1
        return l
