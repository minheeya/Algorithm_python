class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]: #다음날 주식이 오를 경우
                profit += prices[i + 1] - prices[i]
        return profit