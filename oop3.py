# def data_return(arg1, arg2):
#     add = arg1 + arg2
#
#     sub = arg1 - arg2
#     mul= arg1 * arg2
#     div = arg1 / arg2
#     return (add, sub, mul, div)
# a = data_return(5,10)
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
#

x = int(input("enter x"))
y = int(input("enter y"))
z = int(input("enter z"))
if (x > y):
   if (x > z):
    print(f"{x} is large")
else:
    if (y > x):
        print(f"{y} is large")
    else:
        print("z is large")

