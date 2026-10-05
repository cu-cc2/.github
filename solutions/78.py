# Approach 1: Bit Manipulation (Bitmasking)
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


# Approach 2: Backtracking (DFS - Decision Tree)
class SolutionBacktracking:
    def subsets(self, nums):
        subsets = []
        subset = []

        def backtrack(index):
            if index == len(nums):
                subsets.append(subset.copy())
                return

            # Decision 1: Include nums[index]
            subset.append(nums[index])
            backtrack(index + 1)

            # Decision 2: Exclude nums[index]
            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return subsets
