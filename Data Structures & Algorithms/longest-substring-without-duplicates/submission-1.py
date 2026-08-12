class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        keep track of seen w set
        z not in set
        zx ok
        zxy ok
        zxyz z in set so stop here and return zxy
        '''
        seen = set()
        sol = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[right])
            sol = max(sol, len(seen))
        return sol
            