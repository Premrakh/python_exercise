# Exercise 9: Get the key of a minimum value from the following dictionary
d1= {
  'Physics': 82,
  'Math': 65,
  'history': 75,
}
l1=list(d1.values())
l1.sort()
value=l1[0]
for i in d1:
    if d1[i]==value:
        print(i)