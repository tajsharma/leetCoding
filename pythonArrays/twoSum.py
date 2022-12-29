def twoSum(array1, target):
    thisDict = {}
    for number in array1:
        if number not in thisDict:
            thisDict[array1.index(number)] = number
    for i in range(0,len(array1)):
        if target-array1[i] in thisDict:
            return 'yes we have'
    return 'not found bro'

sum1 = 231
array1 = [1,23,42,6,4,5]

print(twoSum(array1,sum1))