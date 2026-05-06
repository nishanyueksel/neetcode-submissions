class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        sol = []
        for i in digits:
            num = num * 10 + i
        num += 1
        while num:
            sol.append(num%10)
            num = num//10
        sol.reverse()
        return sol