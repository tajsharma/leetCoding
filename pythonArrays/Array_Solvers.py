class ArraySolvers:

    def __init__(self):
        pass
    
    def maximum_Subarray_BF(self,nums):
        maxSum = float('-inf')
        currentSum = 0

        for i in range (0,len(nums)-1):
            currentSum += nums[i]
            for j in range(i+1,len(nums)-1):
                currentSum+=nums[j]
                if currentSum > maxSum:
                    maxSum = currentSum
                    print("current max is: ", maxSum)
            currentSum = 0

        return maxSum