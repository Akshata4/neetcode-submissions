class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l, r = 0, 0
        while r < len(s):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            if (r-l+1) - max(cnt.values()) <= k:
                w = (r-l) +1
            else:
                cnt[s[l]] -= 1
                l += 1
            r += 1
        return w
