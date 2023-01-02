# given a n x n 2d matrix , rotate the matrix(representing an image) 90 degrees clockwise
import numpy as np 

def rotate90(matrix):
    left,right = 0, len(matrix)-1

    while left < right:
        for i in range(right-left):
            top, bottom = left, right

            #swap all values 
            topLeft = matrix[top][left+i]
            matrix[top][left+i] = matrix[bottom-i][left]
            matrix[bottom-i][left] = matrix[bottom][right-i]
            matrix[bottom][right-i] = matrix[top+i][right]
            matrix[top+i][right] = topLeft

        #update pointers and these will stop the loop when left crosses right
        right-=1
        left +=1
    print(matrix)


og = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

rotate90(og)