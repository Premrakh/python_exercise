# Exercise 5: Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

chars,digit,symbol=0,0,0
for i in str1:
    if i.isalpha():
        chars+=1
    elif i.isnumeric():
        digit+=1
    else:
        symbol+=1

print(chars)
print(digit)
print(symbol)