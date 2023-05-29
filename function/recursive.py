# Exercise 6: Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10

def fun1(n):
    if n==0:
        return 0
    return n+fun1(n-1)

print(fun1(10))