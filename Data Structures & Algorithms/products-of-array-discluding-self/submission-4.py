class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                product *= i
        output = []
        for i in nums:
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                if i == 0:
                    output.append(product)
                else:
                    output.append(0)
            else: 
                output.append(product//i)
        return output