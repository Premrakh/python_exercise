# Exercise 6: Remove empty strings from the list of strings
l1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i in l1:
    if len(i)==0:
        l1.remove(i)
print(l1)