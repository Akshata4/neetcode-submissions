class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for v, k in enumerate(nums):
            if target - k in seen.keys():
                return [seen[target-k], v]
            seen[k] = v