# Exercise 12: Display Fibonacci series up to 10 terms
n=10
a,b=0,1
print(a)
print(b)
for i in range(n-2):
    c=a+b
    print(c)
    a,b=b,c
