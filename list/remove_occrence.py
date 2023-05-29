# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# Given:

l1 = [5, 20, 15, 20, 25, 50, 20]

num=20                  # which number all occurence you went to remove 
for i in range(l1.count(num)):
    l1.remove(num)
print(l1)
