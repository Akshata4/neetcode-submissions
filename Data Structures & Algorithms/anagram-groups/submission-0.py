class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        curr = 0
        res = {}

        while curr < len(strs):
            s = ''.join(sorted(strs[curr]))
            if res.get(s):
                res[s].append(strs[curr])
            else:
                res[s] = [strs[curr]]
            curr += 1
        return list(res.values())