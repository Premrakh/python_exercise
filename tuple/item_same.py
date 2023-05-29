# Exercise 10: Check if all items in the tuple are the same
t1 = (45, 45, 45, 45)

if t1.count(t1[0])==len(t1):
    print('all items same in tuple')
else:
    print(' Not all items same in tuple')

