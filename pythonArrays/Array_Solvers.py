class ArraySolvers:

    def __init__(self):
        pass
    
    def maximum_Subarray_BF(self,nums):
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum += num 

            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0

        return maxSum 