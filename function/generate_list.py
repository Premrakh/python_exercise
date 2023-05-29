# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

def evenlist(a,b):
    l1=[]
    for i in range(a,b):
        if i%2==0:
            l1.append(i)
    return l1

print(evenlist(4,30))
