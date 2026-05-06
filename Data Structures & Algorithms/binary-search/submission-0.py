class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            midpoint = (start+end)//2
            if nums[midpoint] == target:
                return midpoint
            if nums[midpoint] < target:
                start = midpoint + 1
            else: 
                end = midpoint - 1
        return -1