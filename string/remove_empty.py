# Exercise 14: Remove empty strings from a list of strings
# Given:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

for i in str_list:
    if type(i)==str and len(i)==0:
        str_list.remove(i)
print(str_list)