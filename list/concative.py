# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains 
# the 0th index item from both the list, then the 1st index item, and so on till
#  the last element. any leftover items will get added at the end of the new list.

# Given:

l1 = ["M", "na", "i", "Ke",'123']
l2 = ["y", "me", "s", "lly"]
l3=[]
min,max=l1,l2
if len(l1)>len(l2):
    min,max=l2,l1
for i in range(len(min)):
    l3.append(l1[i]+l2[i])

if len(l1)!=len(l2):
    for i in range(len(min),len(max)):
        l3.append(max[i])
print(l3)


