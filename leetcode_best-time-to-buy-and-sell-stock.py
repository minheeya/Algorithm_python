# 최소 초기값 => sys.maxsize / float('inf')
# 최대 초기값 => -sys.maxsize / float('-inf')
class Solution(object):
    def maxProfit(self, prices):
        
        profit, min_price = 0, sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit