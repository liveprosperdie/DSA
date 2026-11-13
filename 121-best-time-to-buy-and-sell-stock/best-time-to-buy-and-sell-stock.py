class Solution(object):
    def maxProfit(self, prices):
        maximum=0
        lowest=max(prices)
        for x in prices:
            if (x-lowest)>maximum:
                maximum=x-lowest
            if x<lowest:
                lowest=x
        return maximum
            