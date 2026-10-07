class Solution:
    def subsets(self, nums):
        subsets = []
        n = len(nums)
        size = 1 << n
        for i in range(size):
            subset = []
            for j in range(n):
                if (i >> j) & 1:
                    subset.append(nums[j])
            subsets.append(subset)

        return subsets


class SolutionBacktracking:
    def subsets(self, nums):
        subsets = []
        subset = []

        def backtrack(index):
            if index == len(nums):
                subsets.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1)

            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return subsets
