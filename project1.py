import sys
import math
import random
import threading
import time
from functools import reduce




#We will start with variables.
'''
Variables in programming are memory locations that hold a value. 
    Much like in mathematics, where 'X' is primarily the variable of choice, we can make 'X' equal anything.
'''
a = None            #nonetype, has no type.
b = 3               #integer, a whole number with no decimal point. 
c = 9.45            #float or double, a number with a decimal point.
d = 4               
e = "Hello, world!" #string
f = 'f'             #char


#In python, variables are 'weakly typed', meaning the programming langauge declares the variable's type upon value assignment.
    #As a more long-term fact, In a 'strongly typed' language, in order to declare an integer you would go "int x = 5", declaring the datatype, the variable name, and then the value. 


'''
A function is a command, in the form
        name(argument1, argument2, argument3, argumentX, argumentY, argumentZ)
            ^ Parentheses|  ^ Arguments seperated by commas                  ^close parentheses
         ^ Function name |

    Functions are commands that go through a series of steps in order to attain a certain goal.
    print() | Does not print a piece of paper, instead it displays text inside a terminal.
    
'''


def sumVargAndVarv(varg,varv):
    return varg + varv


#We will go more in-depth in them later.

print(  sumVargAndVarv(1,2)   ) #Will print 3
print("Hello, world!") #prints "Hello, world!"
print(e) #Also prints "Hello, world!"
print("Hello, world!" + e) #prints "Hello, world!Hello, world!"
print("Hello, world!", e) #gives us a tuple of value ('hello world', 'hello world')

# The arithmetic operators +, -, *, /, %, **, //
# ** Exponential calculation
# // Floor Division
print("5 + 2  ="+ str(5+2))   #prints 7
print("5 - 2  ="+ str(5-2))   #prints 3
print("5 * 2  ="+ str(5*2))   #prints 10
print("5 / 2  ="+ str(5/2))   #2 goes into 5 only 2 times (4). Therefore, prints 2
print("5 % 2  ="+ str(5%2))   #Since 2 goes into 5 2 times, 2*2 = 4, the remainder is 1. This prints 1.
print("5 ** 2 ="+ str(5**2)) #5^2 = 25
print("10//3.0="+ str(10//3.0))# In math, 10/3 = 3.333333. By using floor division, 10//3 = 3, floor division rounds down to the lower integer.
print("-10//3.0=", str(-10//3.0))# This also means that since -4.0 < -3.33333333 < -3.0, -10//3.0 = -4.0


#if you want to extend a statement to multiple lines, you can use parenthesis, or \

v1 = (
        1+2
        +5
     )

print(v1) #returns 8 as an int

print(
        1+2
        +5
     )#Still returns 8 as an int


#This is nice and all, but what about the max integer or float we can practically return?
#Well, in python this is rather huge.
print(sys.maxsize) #Returns the max size for integer
print(sys.float_info.max) #Returns the max size for float
#HOWEVER, a float is only accurate up to 15 digits
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1+f2
print(1234567890123456)
print(f3)


#complex numbers are in the form [real part]+[imaginary part]
cn1 = 5+6j

#booleans are either True or False
bl = True
bl = False

#Strings are surrounded by ' or "
str1 = "Escape Sequences \' \t \" \\ and \n"
print(str1)
str2 = ''' Triple quoted strings can contain ' and " '''
print(str2)

# Math Functions, we'll just skim over this
print("abs(-1) ", abs(-1))
print("max(5, 4) ", max(5, 4))
print("min(5, 4) ", min(5, 4))
print("pow(2, 2) ", pow(2, 2))
print("ceil(4.5) ", math.ceil(4.5))
print("floor(4.5) ", math.floor(4.5))
print("round(4.5) ", round(4.5))
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0) ", math.radians(0))
print("degrees(pi) ", math.degrees(math.pi))

# You can cast to different types with int, float,
# str, chr
print("Cast ",   type(int(5.4)))  # to int
print("Cast 2 ", type(str(5.4)))  # to string
print("Cast 3 ", type(chr(97)))  # to string
print("Cast 4 ", type(ord('a')))  # to int


# ----- CONDITIONALS -----
# Comparison Operators : < > <= >= == !=
 
# if, else & elif execute different code depending
# on conditions
age = 30
if age > 21:
            # Python uses indentation to define all the
            # code that executes if the above is true
            print("You can drive a tractor trailer")
elif age >= 16:
    print("You can drive a car")
else:
    print("You can't drive")


# Make more complex conditionals with logical operators
# Logical Operators : and or not


if age < 5:
    print("Baby or Preschool")
elif (age >= 5) and (age <= 6):
    print("Kindergarten")
elif (age > 6) and (age <= 17):
    print("Grade %d", (age - 5))
else:
    print("College")
                     
# Ternary operator in Python
# condition_true if condition else condition_false
canVote = True if age >= 18 else False
print(canVote)

# Combine strings with +
print("Hello " + "You")
 
# Get string length
str3 = "Hello You"
print("Length ", len(str3))
 
# Character at index
print("1st ", str3[0])
   
# Last character
print("Last ", str3[len(str3)-1])
  
# 1st 3 chrs
print("1st 3 ", str3[0:3])  # Start, up to not including
     
# Get every other character
print("Every Other ", str3[0:-1:2])  # Last is a step
      
# You can't change an index value like this
# str3[0] = "a" because strings are immutable
# (Can't Change)
# You could do this
str3 = str3.replace("Hello", "Goodbye")
print(str3)


#----------LISTS------------
#A list is a sequence of data, whose placement is defined by a number.
#Said number is a placement, or index.
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

#Lists can be printed in their entirety
print(list1)
#Or specific elements can be printed. Elements start at 0 and end n-1, where n= the length of the list.
print("The length of list1 is = " +str(len(list1)))
print("list2[0]="+ str(list1[0]) + " list2[3]=" +str(list1[3]))


#-----------LOOPS-----------
# While : Execute while condition is True
# While : Execute while condition is True
w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1
 
w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        w2 += 1
        # Skips to the next iteration of the loop
        continue
    w2 += 1
 
# Cycle through list
l4 = [1, 3.14, "Element 2", True]
while len(l4):
    print(l4.pop(0))
 
# For Loop
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
# end="" eliminates newline
for x in range(0, 10):
    print(x, ' ', end="")
print('\n')
 
# Cycle through list
l4 = [1, 3.14, "Element 2", True]
for x in l4:
    print(x)
 
# You can also define a list of numbers to
# cycle through
for x in [2, 4, 6]:
    print(x)



# ----- TUPLES -----
# Tuples are just like lists except they are
# immutable
t1 = (1, 3.14, "tuple[2]", False)
 
# Get length
print("Length ", len(t1))
  
# Get value / values
print("1st", t1[0])
print("Last", t1[-1])
print("1st 2", t1[0:2])
print("Every Other ", t1[0:-1:2])
print("Reverse ", t1[::-1])
   
# Everything you can do with lists you can do with
# tuples as long as you don't change values


# ----- FUNCTIONS -----
# Functions provide code reuse, organization
# and much more
# Add 2 values using 1 as default
# You can define the data type using function
# annotations
def get_sum(num1: int = 1, num2: int = 1):
    return num1 + num2
print(get_sum(5, 4))
 
# Accept multiple values
def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(get_sum2(1, 2, 3, 4))
 
# Return multiple values
def next_2(num):
    return num + 1, num + 2
i1, i2 = next_2(5)
print(i1, i2)
 
# A function that makes a function that
# multiplies by the given value
def mult_by(num):
    # You can create anonymous (unnamed functions)
    # with lambda
    return lambda x: x * num
print("3 * 5 =", (mult_by(3)(5)))
 
# Pass a function to a function
def mult_list(list, func):
    for x in list:
        print(func(x))
mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)
 
# Create list of functions
power_list = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]



'''
Sources: https://www.newthinktank.com/2019/08/learn-python-one-video/
w3schools

'''
