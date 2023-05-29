# Exercise 8: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.

d1 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

old_key='city'
new_key='location'

d1['location']=d1[old_key]
d1.pop('city')
print(d1)