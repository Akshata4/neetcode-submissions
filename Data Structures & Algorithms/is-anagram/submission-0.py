class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## length mismatch
        if len(s) != len(t):
            return False
        hash_s, hash_t = {}, {}

        for i in range(0, len(s)):
            if s[i] in hash_s.keys():
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1
            if t[i] in hash_t.keys():
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]] = 1
        
        if hash_s == hash_t:
            return True
        return False