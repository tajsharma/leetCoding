import numpy as np 


new = np.array([[1,23,44,12],[13,14,20,19],[34,21,21,6],[21,23,29,25]])

neew = np.insert(new,3, [3,3,3,3],axis=0)

def accessElement(row, col, array2d):
    return array2d[row][col]

def printall(array2d):
    for i in reversed(array2d):
        for j in reversed(i):
            print(j)

printall(neew)