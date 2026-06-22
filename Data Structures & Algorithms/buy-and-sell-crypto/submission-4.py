class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        mx = 0
        while s < len(prices):
            print(prices[b], prices[s])
            if prices[b] > prices[s]:
                b = s
                s += 1
            elif prices[s] >= prices[b]:
                mx = max(mx, prices[s]-prices[b])
                s += 1
        return mx