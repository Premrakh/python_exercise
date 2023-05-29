# Exercise 10: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary
d1 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

name='Brad'        #enter a employer name you went to change salary
for i in d1:
    if d1[i]['name']==name:
        d1[i]['salary']=8500

print(d1)