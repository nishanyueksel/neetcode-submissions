class Solution:
    """
    [30,38,30,36,35,40,28]
    30 -> 38 one day, move on
    38 -> 30 not decrease
    keep scanning till 40 which is 5 differece so 5
    
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res



        