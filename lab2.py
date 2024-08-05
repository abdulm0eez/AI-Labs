# While loop
count=5
while(count<5):
    count=count+1
    print(f"count number:{count}")

# Single statement while loop
count=0
while(count==10): print("HELLO")

# For loop
list=["uncharted","god of war"]
for i in list:
    print(i)

# Tuple
tuple=["uncharted","god of war"]
for i in tuple:
    print(i)

# String
string="Moeez"
for i in string:
    print(i)

# Loop Control
# Break
string="Moeez"
for letter in string:
    if letter == "a":
        break

print(f"current letter is:{letter}")

# Continue
string="Moeez"
for letter in string:
    if letter == "a":
        continue

print(f"current letter is:{letter}")

# Functions
def my_function(a):
    print(a)
    print(type(a))

my_function(1.00)

def function(country):
    for i in country:
        print(i)

country = ["pakistan","china","oman"]

function(country)

def func(number):
    return 5*number
print(func(5))

# Keywords arguments
def my_func(game1,game2,game3):
    print("the most popular is:" + game1)
my_func("red dead 2","cricket 24","COD")

# Classes and Objects
# Classes
class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def myfunction(self):
        print(f"my name is{self.name}& age is{self.age}")

P1 = Person("Moeez","22")
P1.myfunction()