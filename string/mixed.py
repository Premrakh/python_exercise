# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the 
# char of s1, then the last char of s2, Next, the second char of s1 and second last
#  char of s2, and so on. Any leftover chars go at the end of the result.
s1 = "Abc"
s2 = "Xyz"
s2=s2[-1::-1]
s3=''
print(s2)
min=len(s1)
if len(s1)>len(s2):
    min=len(s2)
    
for i in range(min):
    s3+=s1[i]+s2[i]

s3+=s1[min::] +s2[min::]
print(s3)