# Exercise 3: Calculate the sum of all numbers from 1 to a given number
n=int(input('enter a number'))
ans=0
for i in range(1,n+1):
    ans+=i
print(f'sum of 1 to {n} is {ans}')
