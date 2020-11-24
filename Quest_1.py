### Quest 1 : Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array ###




import numpy as np 

row= int(input("Insert row : "))
col = int(input("Insert col : "))
 
def d_array(r,c):
    arr1 = [[i*j for j in range(c)] for i in range(r)]
    arr2=np.array(arr1)
    return arr2
 
print(d_array(row,col))
