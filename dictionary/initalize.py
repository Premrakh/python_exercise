# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

d1={}
for i in employees:
    d1[i]=defaults

print(d1)