class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for k in range(len(nums)):
            # Skip duplicate values for k
            if k > 0 and nums[k] == nums[k-1]:
                continue
                
            target = -nums[k]
            i = k + 1  # Start after k
            j = len(nums) - 1
            
            while i < j:
                two_sum = nums[i] + nums[j]
                if two_sum == target:
                    output.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # Skip duplicates for i and j
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif two_sum < target:
                    i += 1
                else:
                    j -= 1
                    
        return output