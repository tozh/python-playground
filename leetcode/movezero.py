class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        count = 0
        while nums[j] == 0:
            j += 1
            count += 1
        while i < len(nums) - count and j < len(nums):
            print(i, j, count)
            nums[i] = nums[j]
            i += 1
            j += 1
            while j < len(nums) and nums[j] == 0:
                j += 1
                count += 1

        while i < len(nums):
            nums[i] = 0
            i += 1
        return nums

s = Solution()
A = [0,1,0,3,12]
s.moveZeroes(A)
print(A)