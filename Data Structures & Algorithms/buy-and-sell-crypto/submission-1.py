class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit = 0
        l, r = 0, 1
        if sorted(prices) == prices[::-1]:
            return 0
        while r<len(prices):
            if prices[l]< prices[r]:
                profit = prices[r]-prices[l]
                MaxProfit = max(MaxProfit, profit)
            else:
                l = r
            r +=1
            # print(l,r)            
        return MaxProfit
