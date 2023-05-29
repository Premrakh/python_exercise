# Exercise 11: Write a program to display all prime numbers within a range
st=int(input('enter a start number: '))
end=int(input('enter a end number: '))
for n in range(st,end+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)

