class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in nums:
            if i - 1 in numSet:
                continue
            streak, curr = 0, i
            while curr in numSet:
                streak+=1
                curr+=1
            longest = max(longest, streak)
        return longest