# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# Given:

l1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:

# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

l1[2][2].append(7000)
print(l1)