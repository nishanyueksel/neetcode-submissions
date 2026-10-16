class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charset = {}
        l = 0
        for r in range(len(s)):
            while s[r] in charset:
                del charset[s[l]]
                l+=1
            charset[s[r]] = 1
            res = max(len(charset), res)
        return res
