# Exercise 18: Replace each special symbol with # in the following string
# Given:

str1 = '/*Jon is @developer & musician!!'
str2=''
punc='''!@#$%^&*()_+*\|><.,/?'":;{][]}'''
for i in str1:
    if i in punc:
        str2+='#'
    else:
        str2+=i
print(str2)
