#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/

"""You have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times)."""

    def maxProfit(self, prices: List[int]) -> int:
        result=0
        if prices==[]:
            return 0
        previous=prices[0]
        for price in prices:
            difference=price-previous
            previous=price
            if difference>0:
                result+=difference
        return result
