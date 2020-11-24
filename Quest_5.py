""" Question 5. Write a snippet that resolves ancient Chinese puzzle:

We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many
rabbits and how many chickens do we have?

Suggestions: You can use "for loop" to iterate all possible conditions.
"""



## Solution
#  Total heads = 35
#  Total legs = 94
#  Total heads with minimum 2 legs so far = 94/2 = 47
#  Rabbits = 47-35 = 12
#  Chicken = 35-12 = 23

a=35
print("Total Heads : ",a)
b=94
print("Total Legs : ",b)

c=a*2
d=(b-c)/2
print("Number of Rabbits present : ",d)
e=a-d
print("Number of Chickens present : ",e)
