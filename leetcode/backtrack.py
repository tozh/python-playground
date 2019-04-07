class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.N = len(nums)
        self.nums = nums
        record = [0 for _ in range(self.N)]
        self.backtrack([], record, 0)
        return self.result

    def backtrack(self, temp_list, record, start):
        if len(temp_list) == self.N:
            self.result.append(temp_list[:])
            return
        for i in range(0, self.N):
            if record[i] == 0:
                temp_list.append(self.nums[i])
                record[i] = 1
                self.backtrack(temp_list, record, i + 1)
                record[i] = 0
                temp_list.pop()

s = Solution()
a = [1, 2, 3]
print(s.permute(a))

