a = 10
print(type(a))
# we can use type function to find the data type
print(dir(a))
# we can use dir function to find object of any data type
x = input("enter any number")
print(x)
# like this way we take input from the user
b = input("enter value of b")
c = input("enter value of c")
print(b+c)
# Python take every input as a string, so result will be different.to solve this problem we have to type casting
# b = int(b)
# c = int(c)
# print(b+c)
b = int(input("enter value of b"))
c = int(input("enter value of c"))
print(b+c)
# or print(int(b) + int(c))
# if we do like print(int(b+c)), output will be 12 if b=1 and c=2