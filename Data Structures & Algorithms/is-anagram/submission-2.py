class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hms = {}
        hmt = {}
        for i in s:
            hms[i] = hms.get(i, 0) + 1
        for j in t:
            hmt[j] = hmt.get(j, 0) + 1
        return hmt == hms