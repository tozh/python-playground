class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(len(nums)):
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < target: # sum shuold be greater
                    result += r - l
                    l += 1
                else:
                    r -= 1
        return result

s = Solution()
s.threeSumSmaller([-2,0,1,3], 2)