#LC 121: Best time to buy and sell a stock
#one pass solution
from asyncio import constants


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


#solves threesum using two pointers
    def threeSum(nums):
        sol = []
        nums.sort()
        for i,a in enumerate(nums):
            if i >0 and a == nums[i-1]: #checks if the value of a is the same as previous
                continue

            l,r = i+1, len(nums)-1 #two pointers approach
            while l<r:
                three = a + nums[l] + nums[r]
                if three > 0:
                    r = r-1
                elif three < 0:
                    l = l+1
                else:
                    sol.append([a,nums[l],nums[r]])#keeps number from repeating in the same sequence
                    l = l+1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
        return sol




#Driver code 
lebron = Solutions


array1 = [-3,3,0,1,2,-1]

print(lebron.threeSum(array1))