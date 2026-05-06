class Solution:
    """
    
    """
    def trap(self, height: List[int]) -> int:
        result = 0
        for i in range(len(height)):
            l = r = height[i]

            for j in range(i):
                l = max(l, height[j])
            for j in range(i + 1, len(height)):
                r = max(r, height[j])
            result += min(l, r) - height[i]
        return result

        