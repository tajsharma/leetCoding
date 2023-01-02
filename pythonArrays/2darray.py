import numpy as np 


new = np.array([[1,23,44,12],[13,14,20,19],[34,21,21,6],[21,23,29,25]])

neew = np.insert(new,3, [3,3,3,3],axis=0)

def accessElement(row, col, array2d):
    return array2d[row][col]

def linearSearch(array2d,num):
    for i in array2d:
        for j in i:
            if j == num: 
                return 'Your element has been found'
    return 'we couldnt find that number boss'


print(len(new))

print(linearSearch(neew,2323))