# Exercise 12: Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string
str1 = "Emma is a data scientist who knows Python. Emma works at google."
find_str='Emma'
ans=str1.rfind('Emma')
print(f'Last occurrence of {find_str} starts at index {ans}')