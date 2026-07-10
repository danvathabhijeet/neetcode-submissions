class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        minimum = 0
        profit = 0
        for _ in range(len(prices)-1):
            if prices[sell]<prices[minimum]:
                minimum = sell
            sell+=1
            profit = max(profit, prices[sell]-prices[minimum])
        return profit

        


