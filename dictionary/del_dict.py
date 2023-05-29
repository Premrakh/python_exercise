# Exercise 6: Delete a list of keys from a dictionary

d1 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
for i in keys:
    d1.pop(i)
print(d1)