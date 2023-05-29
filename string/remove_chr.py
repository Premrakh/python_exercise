# Exercise 16: Removal all characters from a string except integers
# Given:
# output : 2510
str1 = 'I am 25 years and 10 months old'

for i in str1:
    if i.isnumeric():
        print(i,end='')
