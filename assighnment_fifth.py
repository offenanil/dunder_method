num = int(input("Enter Number of Students : "))
increment = 1
studentsMask = []
while increment <= num:
    print(f"=== Student  {increment}===")
    for x in range(1):
        nep = float(input("Enter Nepali marks:"))
        mat = float(input("Enter Maths marks:"))
        eng = float(input("Enter English marks:"))
        pop = float(input("Enter Population marks:"))
        sic = float(input("Enter Science marks:"))
        masks = [nep, mat, eng, pop, sic]
        studentsMask.append(masks)
        increment += 1

    totalMask = []

    for sMask in studentsMask:
        total = 0
        for sm in sMask:
            total += sm
        totalMask.append(total)
    for res in totalMask:
        pre = res / 5
    print(pre)
    print("======Result=====")

    print(f"total:{res}, pre:{pre}")
    print("division")
    if  pre > 35 and pre <= 45:
        print("Third")
    elif pre > 45 and pre <= 60:
        print("Second")
    elif pre > 60 and pre <= 75:
        print("Fisrt")
    elif pre > 75 and pre < 100:
        print(" distiction")
    else:
        print ("Fail")
