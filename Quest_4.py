""" Question 4. Write a code that generates the following pattern based on True or
False conditions.
Expected result of code:
Enter condition: True
    *
   ***
  *****
 *******
*********
Enter condition: False
*********
 *******
  *****
   ***
    *
"""


## For True condition ## 
def truepattern(n):
    for i in range(1,n+1):
        print(" " *(n-i),end="")
        for j in range(1,i+1):
            print("*",end=" ")
        print()
## For False condition ## 
def falsepattern(n):
    for k in range(1,n):
        print(" "*k,end="")
        for l in range(1,n+1-k):
            print("*",end=" ")
        print()

a=int(input("Enter First no : "))
b=int(input("Enter Second no : "))

if a>b: #Given condition#
    truepattern(5)
    print("Given condition is True")
    
else:
    falsepattern(6)
    print("Given condition is False")
