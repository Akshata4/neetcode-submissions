class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for i in nums:
            hm[i] = hm.get(i, 0) + 1
        
        arr = [[v, k] for k, v in hm.items()]

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res