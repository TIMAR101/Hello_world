class Solution:
    def maxProfit(self, prices) -> int:

        day = 0
        profit = 0
        lenprice = len(prices)
        maxprise = max(prices)

        for item in range(lenprice-1):

            minprice = min(prices[:item +1])
            maxprice = max(prices[item+1:])
            minprice > max

            if maxprise <= prices[item]:
                continue

            elif prices[item] == maxprise:
                maxprise = prices[item+1:]
                continue

            newprofit = maxprise - prices[item]

            if newprofit > profit:
                    profit = newprofit

        return profit

    def maxProfit1(self, prices):

         buy_price = prices[0] # at the begining the minimum price is the first price
         profit = 0 # at the begining the minimum  profit is zero

         for i in range(1,len(prices)):
            #if the current price is less than the previous buy price ; update the buy_price
            curprice = prices[i]
            if curprice < buy_price:
                buy_price = curprice
            else: # if not check if you sell with the current price would you get better profit than the previous one
                profit = max(profit, curprice-buy_price) # compare the previous profit with the current profit

         return profit









S1 = Solution()

print(S1.maxProfit1(prices = [7,1,5,3,6,4]))




