# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

# Given:

numbers = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(numbers)):
    numbers[i]=numbers[i]**2
print(numbers)