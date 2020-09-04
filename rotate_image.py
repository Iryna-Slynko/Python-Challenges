'''You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]] '''

import copy

def rotateImage(a):
    b=copy.deepcopy(a)
    for i in range (0, len(a)):
        for j in range(0, len(a)):
                b[j][len(a)-1-i]=a[i][j]
    
    return b     
