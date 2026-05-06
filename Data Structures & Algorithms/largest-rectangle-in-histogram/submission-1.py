class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: 
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                top = stack.pop()
                h = heights[top]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, width*h)
            stack.append(i)
        return max_area