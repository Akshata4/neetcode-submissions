class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        mx = 0
        cl = 0

        while curr < len(nums):
            if nums[curr] == 1:
                cl += 1
            else:
                mx = max(mx, cl)
                cl = 0
            curr += 1
        return max(mx, cl)