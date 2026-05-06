class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol_dict = {}
        for i in nums:
            if i in sol_dict:
                sol_dict[i] +=1
            else:
                sol_dict[i] = 1
        sorted_list = dict(sorted(sol_dict.items(), key=lambda item: item[1]))
        sorted_items = list(sorted_list.keys())[-k:]
        return sorted_items