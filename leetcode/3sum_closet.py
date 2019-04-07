class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res_min = 1000000000
        result = []
        for i in range(len(nums)):
            tar = target - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                print(i, result)
                res = tar - nums[l] - nums[r]
                if abs(res) < res_min:
                    res_min = abs(res)
                    result = [nums[i], nums[l], nums[r]]
                if res > 0:
                    l += 1
                elif res < 0:
                    r -= 1
                else:
                    return result
        return sum(result)

s = Solution()
print(s.threeSumClosest([0,2,1,-3], 1))