#LC 121: Best time to buy and sell a stock
#one pass solution
class Solutions:
    def bestTime(prices):
        maxProfit = 0
        minimum = 100000
        for i in range(0,len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                maxProfit = max(maxProfit,prices[i]-minimum)
        return maxProfit

lebron = Solutions

print(lebron.bestTime([10,1,9,3,5,12,2]))