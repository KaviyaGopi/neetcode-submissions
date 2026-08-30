class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Step 2: Build frequency counts for both strings
        countS = {}
        countT = {}

        for char in s:
            countS[char] = countS.get(char, 0) + 1

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        # Step 3: Compare both dictionaries directly
        return countS == countT
        