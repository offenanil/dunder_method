data = [
    ['ram','sita','gita','rita'],
    ['anita', 'asmita','shyam','suman'],
    ['pawan', 'hari','siva','kabita']
]
# if we just want to print suman which is in 1st index of 3rd index row so
print(data[1][3])
data = ['abc', ['sita']]
# print(data[0][0][2])
print(data[0])
# we can replace any data in list shown as below
users = ['ram','sita','gita','hari']
# if i want to replace sita with arun
users[1] = 'arun'
print(users)
# we can add anything on list by using .append function
users.append('hello')
print(users)
users.append(9)
print(users)
data = []
data.append('ram')
print(data)
data.append('mahesh')
print(data)
# how to find index in list
uSers = ['ram','hari','sita','rita']
print(uSers.index('sita'))
# Tuple: tuple is same like list[] but it has bracket () and it is not mutable ie we cannot change the index position at any time
users = ('ram','sita','gita','hari')
print(users[1])
# set{}: it doesnot print duplicate data
data = {'ram','sita','gita','hari','ram'}
print(data)
# dictonary{}
user = {'name': 'anil','age': 28,'phone':9841477}
print(user)