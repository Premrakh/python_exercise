# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned 
# keys from the below dictionary.
d1 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
d2={}
# Keys to extract
keys = ["name", "salary"]

for i in keys:
    d2[i]=d1[i]
print(d2)
