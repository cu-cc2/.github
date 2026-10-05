class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        curr = []
        n = len(candidates)

        def dfs(curr_sum=0, i=0):
            if curr_sum == target:
                ans.append(curr.copy())
                return
            if i == n or curr_sum > target:
                return

            curr.append(candidates[i])
            dfs(curr_sum + candidates[i], i)
            curr.pop()

            dfs(curr_sum, i + 1)

        dfs()
        return ans
