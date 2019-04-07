class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxs = []
        left = []
        right = []
        n = len(nums)
        res = n % k
        time = n // k
        for i in range(time):
            for j in range(k):
                if i * k + j > n:
                    break
                if j == 0:
                    left[i * k + j] = nums[i * k + j]
                else:
                    left[i * k + j] = max(nums[i * k + j], left[i * k + j - 1])
        for i in range(time):
            for j in range(k, -1, -1):
                if i * k + j > n:
                    continue
                if i * k + j == n-1 or j == k-1:
                    right[i*k+j] = nums[i*k+j]
                else:
                    right[i*k+j] = max(nums[i*k+j], right[i*k+j+1])

        for s in range(n):
            if s + k - 1 < n:
                maxs.append(max(left[s + k - 1], right[s]))
        return maxs
