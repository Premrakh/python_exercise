# Exercise 15: Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician"
punc='''!@#$%^&*()_+*\|><.,/?'":;{][]}'''
str2=''
for i in str1:
    if i not in punc:
        str2+=i
print(str2)