class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            k = []
            while s[i] != "#":
                k.append(s[i])
                i += 1
            k = int(''.join(k))
            i += 1
            word = s[i:i+k]
            decoded.append(word)
            i += k
        return decoded

            

            







