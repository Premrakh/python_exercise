# Exercise 3: Create a new string made of the first, middle, and last
#  characters of each input string
s1 = "America"
s2 = "Japan"
# output = AJrpan
ans=s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1]
print(ans)