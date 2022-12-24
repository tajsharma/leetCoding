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

#5 use extend method to add multiple values
arr2 = array('i',[23,6,45,34,11])
arr1.extend(arr2)
print(arr1)


#6 add items to array from a list using fromlist()
listDec = [1,11,21]
arr1.fromlist(listDec)
print(arr1)

#7 remove an element with remove
arr1.remove(124)

#8 remove last array element using pop
arr1.pop()

#9 fetch an index of an element using index() method
print(arr1.index(23))

#10 reverse a python list using reverse()
arr1.reverse()
print(arr1) 

#11 get array buffer info : gives location of the array as well as the length
print(arr1.buffer_info())

#12 check for # of occurances using count()
print(arr1.count(11))