class Solution:
    """
    [30,38,30,36,35,40,28]
    30 -> 38 one day, move on
    38 -> 30 not decrease
    keep scanning till 40 which is 5 differece so 5
    
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)
        for i in range(n):
            counter = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j+=1
                counter+=1
            counter = 0 if j == n else counter
            result.append(counter)
        return result

