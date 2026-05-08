class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        l,r = 0, 1

        ## check profit - p = r-l
        ## if p > max: keep l, move right
        ## else move both l and r

        while r != len(prices):
            p = prices[r] - prices[l]
            print(prices[r], prices[l], p, mx)
            if prices[l] < prices[r]:
                mx = max(mx, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return mx