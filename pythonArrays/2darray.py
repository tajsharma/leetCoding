import numpy as np 


new = np.array([[1,23,44,12],[13,14,20,19],[34,21,21,6],[21,23,29,25]])

neew = np.insert(new,3, [3,3,3,3],axis=0)

def accessElement(row, col, array2d):
    return array2d[row][col]

rowN = int(input("enter the row number u want to see"))
colN = int(input("now enter the column number"))

print("The number u landed on is: ", accessElement(rowN,colN, new))