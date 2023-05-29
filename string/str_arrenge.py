# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program 
# arrange the characters of a string so that all lowercase letters should come first.

str1 = 'PyNaTive'
s1=''
s2=''
for i in str1:
    if i.islower():
        s1+=i
    else:
        s2+=i
print(s1+s2)