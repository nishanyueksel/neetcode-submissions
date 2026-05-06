class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        
        # Sorted pairs: [(num, freq), ...]
        s = sorted(counts.items(), key=lambda x: x[1])
        
        # Get last k pairs (highest frequencies)
        return [num for num, freq in s[-k:]]
