class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]
        for a in prices:
            profit = max(profit, a-buy)
            buy = min(buy, a)
        return profit
