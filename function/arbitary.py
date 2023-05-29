# Exercise 2: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of
#  arguments and print their value.

def fun1(*a):
    for i in a:
        print(i)

fun1(10,20,30,40)