# Exercise 8: Sort a tuple of tuples by 2nd item

t1 = (('a', 23),('b', 37),('c', 11), ('d',29))

t1=list(t1)
t1.sort(key=lambda a:a[1])
t1=tuple(t1)
print(t1)
