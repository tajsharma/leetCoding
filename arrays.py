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



# CTCI 1.3 : method to replace white space with %20 
#takes in a string and a given length, makes a shallow copy of the list
#with the given length parameters; gives back a list of given length
    def URLify(sent, length):
        return sent[:length].replace(' ', '%20')



#Driver code 
lebron = Solutions

string1 = "Mr John Smith    "
print(lebron.URLify(string1,13))
