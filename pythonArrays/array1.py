from array import *

#1 create the array
arr1 = array('i',[77,23,13,124])


#2 traverse the array and print each element
for i in range(0,len(arr1)):
    print(arr1[i])

#3 appned a value to the array
arr1.append(99)


#4 insert a value into the array after the index provided
arr1.insert(1,69)
print(arr1)