# Exercise 7: Check if a value exists in a dictionary
d1 = {'a': 100, 'b': 200, 'c': 300}

value=200                  #enter value you went to check present in dict or not

if value in d1.values():
    print(f'{value} present in dictionary')
else:
    print(f'{value} absent in dictionary')