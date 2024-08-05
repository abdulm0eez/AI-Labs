#Program to find numbers divisible by 7 and multiple of 5 between range of 1500 and 2700


for i in range (1500,2701):
    if (i%7==0) and (i%5==0):
        print(i)


#Converter for temperature


def convert_celsius_to_fahrenheit(celcius):
    "convert celsius to fahrenheit"
    fahrenheit=(9/5)*(celcius+32 )
    return fahrenheit

def convert_fahrenheit_to_celcius(fahrenheit):
    "converts fahrenheit to celsius"
    celsius=(5/9)*(fahrenheit-32)
    return celsius
#get user input
temperature_value=float(input("enter the temperature value"))
temperature_unit=input("enter the unit(C for celsius, F for fahrenheit)".upper)
#perform conversion and print result
if temperature_unit=='C':
    converted_temperature=convert_celsius_to_fahrenheit(temperature_value)
    print(f"{temperature_value}degree celsius is equal to{converted_temperature}degrees fahrenheit")
elif temperature_unit=='F':
    converted_temperature=convert_fahrenheit_to_celcius(temperature_value)
    print(f"{temperature_value}degree fahrenheit is equal to{converted_temperature}degree celsius")
else:
    print("invalid unit enter C or F ")


#Pogram to guess a number between 1 to 9


x=5
while True:
    guess= int(input("guess a number between 1 to 9"))
    if guess==x:
        print("congratulations! you guessed a number")
        break
    else:
        print("try again!")


#Design a pattern using nested loop


    #pattern increasing
    for i in range(1,6):
        for j in range(i):
            print("*", end="")
        print()
    #pattern decreasing
    for i in range(4,0,-1):
        for j in range(i):
            print("*", end="")
        print()


#Reverse the accepted words from the user


x=input("enter a word")
reversed_word=reversed(x)
print(''.join(reversed_word))


#Program that count number of even and odd numbers from a series of numbers


numbers=(1,2,3,4,5,6,7,8,9)
count_even=0
count_odd=0
for i in numbers:
    if i%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print(f'"count_even:"{count_even} "count_odd:"{count_odd}')

    
#Program which prints item and its type from list

list = [1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":'V', "section":'A'}]
print(list[2])
print(type(list[2]))


#Program which prints all numbers from 0 to 6 except 3 and 6 (use continue statement)


for i in range(0,7):
  if i == 3 or i == 6:
    continue
  else:
   print(i)


#Program to get the fibonacci series between 0 to 50
#Fibonacci series: next number is the sum of previous two numbers


list = []
for i in range(0,50):
  list.append(i)

number_previous =list[0]
number_current_previous = list[1]

fibonacci_list = [0,1]
for i in range(3,11):
  fib_num = number_previous+number_current_previous
  fibonacci_list.append(fib_num)
  number_previous = number_current_previous
  number_current_previous = fib_num
print(fibonacci_list)


#Program which prints "Fizz" for numbers of multiple of 3 and print "Buzz" for multiple of 5 and print "FizzBuzz" for both


for i in range(1,51):
    if i%3==0:
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)


#Program that accepts sequence of character lines and prints in lower case


string= 'I am Abdul Moeez'
print(string.lower())


#Program which accepts a binary number of 4 digits and print which is divisible of 5


list = []
for i in range(1,5):
  x = int(input("plz enter 4 digits binary numbers : "))
  list.append(x)

print(list)
for i in range(len(list)):
  if int(list[i])%5==0:
    print(list[i])


#Program that accepts a tring and count alphabets and digits in it


string = "Python 3.2 "
count_alpha = 0
count_digit = 0
for char in string:
  if char.isalpha():
    count_alpha += 1
  elif char.isdigit():
    count_digit += 1
print("Letters: ", count_alpha)
print("Digits: ", count_digit)


#Program takes row(m) and column(n) as input and generates two_dimensional array and elements should be i*j


#get input for number of rows and columns
m= int(input("enter number of rows"))
n= int(input("enter number of columns"))

#create a 2D array filled with zeros
array_2d = [[0 for j in range(n) for i in range(m)]]

#fill the array eith i*j
for i in range(m):
   for j in range(n):
      array_2d[i][j]=i*j

#print 2D array
print(array_2d)



