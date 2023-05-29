# Exercise 4: Concatenate two lists in the following order
l1 = ["Hello ", "take "]
l2 = ["Dear", "Sir"]

# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
l3=[]
for i in l1:
    for j in l2:
        temp=i+j
        l3.append(temp)
print(l3)