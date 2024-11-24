# hello world - the obvious and some language structure play.

print ("hello world")

# continuation :
the_world_is_flat = True
if the_world_is_flat:
    print("flat earthers suck!")

# only works in the interpreter cli - can be used as a calculator
2 * 40

# strings
print('spam eggs in single quotes')
print("spam eggs in double quotes")
print("\"spam eggs in escaped double quotes\"")
print("spam eggs \n on two lines")
print("""multi-line
      to save on using special characters""")

# working with strings
#  string are immutable
word = "Python"
print ('single char ', word[3], 'slice', word[2:4])

# lists
mylist = [1, 2, 3]
print ('the list' , mylist)

# lists are passed by reference - mods to one list will modify them
otherlist = mylist
mylist[1] = 5
print ('the other list', otherlist)

# copy a list - use full slice
listcopy = mylist[:]
mylist[1] = 7
print ('listcopy ', listcopy, 'original list ', mylist)

# add to a list
mylist.append(8)
print ('mylist ', mylist)

# tuple - basically dimension structure - can be nested
iamtuple1 = 1, 2, 3
iamtuple2 = 1, (1, 2 , 3)
iamtupleoflists = [1, 2] , [3, 4]
iamtupleofdictionaries = {"name": "chris", "age": 57}, {"name": "roy", "age": 60}

# dictionaries can be dynamically created (comprehensions)
print (dict(sape=4139, guido=4127, jack=4098))

# loops

# while - fibonacci
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# print with something other than newline
a, b = 0, 1
list = []
while a < 10000000:
    print(a, end=',')
    list.append(a)
    a, b = b, a+b
print ('\n', list)

# if / input
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for - only iterates lists/collections/sequences
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# for with collections
    
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# for with range
#   note - range behaves like a list/collection but does not generate the actual list
for i in range(100):
  print("range num: ", i)

# range with  start/end/increment - 0 based
for i in range(-10, -100, -30):
    print("range again: ", i)

# math with a range 
print("sum of ....", sum(range(1000000)))
print("max of ....", max(range(1000000)))

# do nothing - usefull for manual wait loops or stubbing code
pass

# functions

# simple function
def func(a, b):
    return a + b

print("sum is ", func(1,3))

# match statement - like switch/case statements but based on pattern match vs scalar

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 200:
            return "all good!!!"
        case _:
            return "Something's wrong with the internet"
        
httpResults = [200, 400, 404, 418, 200, 500, 502]

for reqResult in httpResults:
  print("request result ", http_error(reqResult))

# match can unpack like everything else
point = (0,0)  

print("and the point is at...") 

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# default function arguments
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("how are you")
ask_ok("how is it",1,reminder='really!!??')

# note - parm default value is evaluated only once - for lists etc this gives unexpected results
#  the function below returns [1], [1,2] etc NOT [1] [2] [3]
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# generator function

def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")


# TODO usage code for the generator function

# 
# classes - the obvious object oriented constructs
#

# simplest form all derive from object both the below are the same
class Foo:
    pass

class Bar(object):
    pass

# inheritance
class Plant:
    pass

class Tree(Plant):
    pass

# constructor / attributes / methods - these are in the class "suite" aka namespace
del(Plant)  # this deletes a variable/class declaration
del(Tree)

class Plant:
    # constructor - good practice to have one but not mandatory for POCO type usages
    def __init__(self):
        self.data = ['test']
    
print(Plant().data)
print(Plant())

class Dog:

    genus = 'Canine' # class variable - shared by all instances

    def __init__(self, name, tricks = []):
        self.name = name  # instance variables - scoped to current instance
        self.tricks = tricks    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Rover')
e = Dog('Lenny', ['yap', 'fetch'])

d.add_trick('Roll over')
e.add_trick('give paw')

print(d.name, d.tricks, d.genus)
print(e.name, e.tricks, e.genus)

#
# modules - allows namespacing / separating re-usable code 
#   there is also a package concept which allows sub-modules
#

import fibo as fibbo

print(fibbo.fib(4))

from fibo import fib, fib2

print(fib(4))
print(fib2(1000000))
