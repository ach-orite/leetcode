class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
            return nums
        else:
            for i in range(len(nums)):
                if i != 0 and nums[i] == nums[i - 1]: continue
                else:
                    self.dfs(nums[:i]+nums[i+1:], res, path+[nums[i]])



nums = [1, 2, 2]
sl = Solution()
print(sl.permuteUnique(nums))