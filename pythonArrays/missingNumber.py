import numpy as np 

def missing(array):
  #  array.sort()
    sum1 = 0
    for i in range(0,len(array)+1):
        sum1 += i
    
    if(sum1 != sum(array)):
        return abs(sum1 - sum(array))
    else:
        return 'No missing number'




array1 = [0,1,2,3,5]
print(missing(array1))