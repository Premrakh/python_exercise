# Exercise 1A: Create a string made of the first, middle and last character
# input : str1 = "James"
# output : Jms

str1='James'
ans=str1[0]+ str1[len(str1)//2] + str1[-1]
print(ans)