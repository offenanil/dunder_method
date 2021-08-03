
question = input("do you have an account? y/n")
if question == 'n':
    file = open("register.txt", 'w')
    ask = input("do yo wanna create account: 1 for yes and other for exit")
    if ask == "1":
        def register():

            username = input('enter username')
            password = input('enter password')
            a = file.write(f"username= {username}\n")
            b = file.write(f"password= {password}")
            # return a


        register()
        # file.close()
    else:
        pass
    file.close()
elif question == 'y':
    fil = open("register.txt", 'w')
    def login():


        username = input("enter you username")
        password = input("enter you password")
        c = fil.write(f"your username is {username}\t")
        d = fil.write(f"your password is {password}")
    login()
else:
    exit()
fil.close()











