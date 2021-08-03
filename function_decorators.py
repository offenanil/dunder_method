def get_age(age):
    def inner_fun(age):
        if age < 18:
            return "you are not allowed"
        elif age >18 and age < 40:
            return "you are welcome"
        else:
            return "you are not welcome"
    return inner_fun

@ get_age
def check(age):
    return age
print(check(10))