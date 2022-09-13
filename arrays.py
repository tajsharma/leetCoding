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



    
    def productExceptSelf(nums):
        prefix = [1] * len(nums)
        for i in range (1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]      
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= suffix
            suffix = suffix * nums[i]
        return(prefix)



#Driver code 
lebron = Solutions


array1 = [1,2,3,4]

print(lebron.productExceptSelf(array1))