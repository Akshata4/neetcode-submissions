class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return
        seen = {}

        for i in range(len(nums)):
            if (target - nums[i]) in seen.keys():
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i
        