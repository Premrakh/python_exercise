# Exercise 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 
# in the middle of s1.

s1 = "Ault"
s2 = "Kelly"
# output : AuKellylt

first=s1[0:len(s1)//2]
last=s1[len(s1)//2:]
new_str=first+s2+last
print(new_str)