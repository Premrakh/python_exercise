# Exercise 1: Create a list by picking an odd-index items from the first 
# list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3=[]
l4=[]
for i in range(len(l1)):
    if i%2!=0:
        l3.append(l1[i])
    else:
        l4.append(l2[i])
print(l3+l4)

