class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        f, l = 0, 1
        if len(set(s)) == 1:
            return 1
        while l < len(s):
            # mx = max(mx, (l-r)+1)
            if len(s[f:l+1]) == len(set(s[f:l+1])):
                ## move l
                l += 1
                mx = max(mx, (l-f))
            else:
                l += 1
                f += 1
        return mx
            


        # print(s[f:l+1])