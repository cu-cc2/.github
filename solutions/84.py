from collections import deque


class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = deque()
        mx = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                mx = max(mx, height * width)
            stack.append(i)

        return mx
