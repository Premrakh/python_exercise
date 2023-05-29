# Exercise 9: Find the largest item from a given list
def max(l1):
    ans=l1[0]
    for i in range(len(l1)):
        if ans<l1[i]:
            ans=l1[i]
    return ans

print(max([4, 6, 8, 24, 12, 2]))
        
                

