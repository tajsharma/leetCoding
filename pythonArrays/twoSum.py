def twoSum(array1, target):
    thisDict = {}
    for number in array1:
        if number not in thisDict:
            thisDict[number] = number
    for i in range(0,len(array1)):
        if target-array1[i] in thisDict:
            return thisDict[target-array1[i]], thisDict[array1[i]]
    return 'not found bro'

sum1 = 10
array1 = [1,23,42,6,4,5]
print(twoSum(array1,sum1))

