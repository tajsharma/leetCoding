#given an array of postive integers, return the highest product of 2 numbers
def maxProduct(list1):
    largest = list1[0]
    maxProd = 0
    for i in range(0,len(list1)):
        product = largest * list1[i]
        if product > maxProd:
            maxProd = product
        if list1[i]> largest:
            largest = list1[i]
    return maxProd


pray4love = [9,10,2,10,17,38]
print(maxProduct(pray4love))