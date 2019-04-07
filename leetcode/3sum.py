import threading
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        if nums[0] > 0:
            return result
        if nums[0] == 0:
            if nums[2] == 0:
                result.append([0, 0, 0])
            return result
        zero_s = -1
        zero_t = -1
        for i in range(len(nums)):
            if nums[i] >= 0 and nums[i - 1] < 0 and zero_s == -1:
                zero_s = i
            if nums[i] > 0 and nums[i - 1] <= 0 and zero_t == -1:
                zero_t = i
        print(zero_s, zero_t)
        if zero_s == -1:
            return []

        if zero_t - zero_s >= 3:
            result.append([0, 0, 0])
        i = 0
        while i < zero_s:
            if i < zero_t - 1 and nums[i] == nums[i + 1]:
                i += 1
                continue
            target = -nums[i]
            d = {}
            j = zero_t
            while j < len(nums):
                if nums[j] == target and zero_s != zero_t:
                    if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                        continue
                    else:
                        result.append([nums[i], 0, nums[j]])
                else:
                    if nums[j] in d:
                        if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                            j += 1
                            continue
                        else:
                            result.append([nums[i], d[nums[j]], nums[j]])
                    else:
                        d[target - nums[j]] = nums[j]
                j += 1
            i += 1
        j = zero_t
        while j < len(nums):
            if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                j += 1
                continue
            target = -nums[j]
            d = {}
            i = 0
            while i < zero_s:
                if nums[i] in d:
                    if i < zero_s - 1 and nums[i] == nums[i + 1]:
                        i += 1
                        continue
                    else:
                        result.append([nums[i], d[nums[i]], nums[j]])
                else:
                    d[target - nums[i]] = nums[i]
                i += 1
            j += 1
        return result


nums = [-1, 0, 1, 0]
s = Solution()
print(s.threeSum(nums))
