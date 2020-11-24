""" Question 3. Write a code that accepts the 2 lists and generates the following
result.
Employee = [‘Amit’,’Manish’,’Mahi’,’Kirti’,’Mafin’]
Salary = [20000,30000,20000,40000,25000]
Expected result of code:
{‘Amit’:20000,’Manish’:30000,’Mahi’:20000,’Kirti’:40000,’Mafin’:25000 }"""


keys=[]
values=[]
n=int(input("Enter number of employees:"))

print("For Employees :")
for x in range(0,n):
    element=input("Enter employee name" + str(x+1) + ":")
    keys.append(element)
    
print("For Salary:")
for x in range(0,n):
    element=int(input("Enter employee salary" + str(x+1) + ":"))
    values.append(element)
    
d=dict(zip(keys,values))
print("The data for employees is:")
print(d)
