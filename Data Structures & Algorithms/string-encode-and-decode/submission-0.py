class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 

    def decode(self, s: str) -> list[str]:
        res, i = [], 0

        while i < len(s):          # Fixed: s instead of str
            j = i
            while s[j] != "#":     # Fixed: s instead of str
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])  # Fixed: s instead of str
            i = j + 1 + length
        return res                 # Fixed: res instead of result