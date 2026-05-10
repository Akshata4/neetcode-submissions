class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        mx = -1
        i = len(arr) - 1
        while i >= 0:
            res = [mx] + res
            mx = max(arr[i], mx)
            i -= 1
        return res
        



