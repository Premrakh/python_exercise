# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and 
# if it is present, replace it with 200. Only update the first occurrence of an item.

# Given:
num=20
new_value=200
l1 = [5, 10, 15, 20, 25, 50, 20]
if num in l1:
    l1[l1.index(num)]=new_value
print(l1)
        

