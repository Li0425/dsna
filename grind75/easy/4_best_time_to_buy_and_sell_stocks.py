from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10**4
        for price in prices:
            curr_profit = price - min_price
            max_profit = max(curr_profit, max_profit)
            min_price = min(min_price, price)
        
        return max_profit
