# Exercise 10: Write a program to count occurrences of all characters within a string
s1='Apple'
d1={}
for i in s1:
    if i not in d1:
        d1[i]=s1.count(i)
print(d1)