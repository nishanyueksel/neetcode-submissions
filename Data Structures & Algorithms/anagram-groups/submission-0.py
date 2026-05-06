class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for i in strs:
            signature = "".join(sorted(i))
            if signature in my_dict:
                my_dict[signature].append(i)
            else: 
                my_dict[signature] = [i]
        return list(my_dict.values())
            
        

        