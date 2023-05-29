# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that
#  appear in the string, ignoring all other characters.
str1 = "PYnative29@#8496"
div=0
sum=0
for i in str1:
    if i.isnumeric():
        sum+=int(i)
        div+=1
print(f'sum is: {sum} avarage is: {sum/div}')
