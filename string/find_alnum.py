# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.

# Given:


str1 = "Emma25 is Data10 scientist50 and AI Expert"

l1=str1.split()
for i in l1:
    if i.isalnum() and i.isalpha()==False:
        print(i)