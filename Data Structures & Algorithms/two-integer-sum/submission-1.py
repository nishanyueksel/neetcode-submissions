class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        random = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in random:
                return [random[complement], i]
            else:
                random[nums[i]] = i
        return []
        