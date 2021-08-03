num = int(input("enter any number:"))
x = 1
while x <= num:
    if x % 2 == 0:
        print(f' even number is: {x}')
    elif x % 2 != 0:
        print(f'odd number is: {x}')
    x = x + 1

else:
    print('enter valid number')