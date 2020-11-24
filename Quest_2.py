""" Question 2. Assume some email address like "username@companyname.com",
now write a snippet that extracts the company name of a given email
address.
expected result of code:
Enter your email: shubhamb@techspawn.com
Your company name is: techspawn """




import re
email = input("Enter email id : ")
name=re.findall(r'\w+[.]', email)[0][:-1]
print("Name of the company is : ",name.capitalize())
