#create an algorithm that checks if a a pyhon list contains all unique numbers
def allUnqiue(list1):
    newList = []
    for i in range(0,len(list1)):
        if list1[i] in newList:
            return 'contains duplicate'
        else:
            newList.append(list1[i])
    return 'All uniques'

myList = [1,2,3,1]
print(allUnqiue(myList))