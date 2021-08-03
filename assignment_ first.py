nep = input("enter marks of nepali")
nep = int(nep)
print(nep)
eng = input("enter marks of english")
eng = int(eng)
print(eng)
mat = input("enter marks of math")
mat = int(mat)
print(mat)
sci = input("enter marks of science")
sci = int(sci)
print(sci)
pop = input("enter marks of population")
pop = int(pop)
print(pop)
total_marks = int(nep+eng+mat+sci+pop)
print(total_marks)
percentage = float(total_marks/5)
print(percentage)
if percentage < 35:
    print('fail')
elif percentage > 35 and percentage < 45:
    print('third division')
elif percentage > 45 and percentage < 60:
    print('second division')
elif percentage > 60 and percentage < 75:
    print('first division')
elif percentage > 75 and percentage < 100:
    print('top')
else:
    print('enter marks of each subjects in between 0 to 100')
