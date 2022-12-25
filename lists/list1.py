list1 = [1,2,3,5,9,123,32,14,45,69,345]
list1.sort()


def binarySearch(list,value): # NEED TO COME BACK AND FIX THIS ONE
    midIndex = len(list1)//2
    if list[midIndex] == value:
        return 'Value has been found'
    elif list[midIndex] > value:
        return binarySearch(list[0:midIndex-1],value)
    else:
        return binarySearch(list[midIndex+1:len(list)],value)
    
    


binarySearch(list1,123)