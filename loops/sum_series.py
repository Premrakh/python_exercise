# Exercise 17: Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term. For example,
#  if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

n=5
num=2
ans=0
temp=2
for i in range(n):
    ans+=temp
    print(temp)
    temp=temp*10+num
print(ans)
