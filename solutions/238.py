class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = right = 1
        ans = nums.copy()
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans
