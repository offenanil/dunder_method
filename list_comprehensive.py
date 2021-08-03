# list comprehension in python means unique way to quickly creating list with python
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
# short cut way
mylist = [letter for letter in mystring]
print(mylist)
# another example in different way: remember ...both variable name have to be same like letter and letter in above case and x n x in bellow case
mylist = [x for x in 'word']
print(mylist)
# another example
mylist = [ y for y in range (0, 11)]
# range(a,b,c):- a:where to start, b:ending point but not including that value, c: step size
print(mylist)
# another example
mylist = [z**2 for z in range(0, 11) ]
print(mylist)
# another example
# finding even numbers
mylist = [s for s in range(0, 11) if s%2 == 0]
print(mylist)
# converting celcius into fahrenheit
celcius = [0, 10, 20, 30.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)
# another example
results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)


