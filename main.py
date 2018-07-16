# Main file of the Python program.
def printSleep(x, end='\n'):
    import time

    s = str(x)
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.3)
        print('', end)


printSleep("Hello World!")
printSleep(3 * 5)
a = 10.0 / 3.0
printSleep(10.0 / 3.0)
printSleep(a + a == 20 / 3.0)
"""
This is a
multilline comment
  Addition (+), subtraction (-), multiplication (*), division (/), modulo (%) and power (**) 
  operators are built into the Python language.
  
This means you can use them right away. If you want to use a square root in your calculation, 
you can either raise something to the power of 0.5 or you can import the math module. 
Do not worry about what it means right now, we will cover this later during the course. 
Below are two examples of square root calculation: 
"""
print(9 ** 0.5)  # calcolo radice quadrata

# alternativa

import math  # https://docs.python.org/3/library/math.html

print(math.sqrt(16))

print(math.log(16, 2))
print(math.log(27, 3))

print(math.sin(0))

print(math.asin(1))
print(math.pi)
print(math.acos(1 / 2) * 2)  # in radianti

print((math.cos(3.4) ** 2) + (math.sin(3.4) ** 2))
# programma manipola oggetti scalari e non e hanno un tipo che definisce che cosa e' possibile fare

print(type(5))
print(type(5.3))

x = int(input('Enter an integer: '))
printSleep('SIMPLE CONDITIONALS')
if x % 2 == 0:
    printSleep('')
    printSleep('Even')
else:
    printSleep('Odd')
printSleep('Donewith conditional')
printSleep('NESTED CONDITIONALS')
if x % 2 == 0:
    if x % 3 == 0:
        printSleep('Divisibile per 2 and 3')
    else:
        printSleep('Divisibile per 2 and not by 3')
elif x % 3 == 0:
    printSleep('Divisiblebile per  3 and not by 2')
printSleep('While loop')

a = x
while x > 0:
    printSleep(x)
    x = x - 1

printSleep('FOR')
for i in range(a):
    printSleep(i)

for i in range(4, 9, 2):
    printSleep(i)
varA = 1
varB = "Ciao"
if type(varA) == str or type(varB) == str:
    printSleep("string involved")
elif varA > varB:
    printSleep("bigger")
elif varA == varB:
    printSleep("equal")
else:
    printSleep("smaller")
"""
Positive root of the following equation: 34*x^2 + 68*x - 510
Recall: given a*x^2 + b*x + c, 
then x = (-b +sqrt(b*b - 4*a*c))/(2*a)
import math
math.cos(3.4)**2+math.sin(3.4)**2
"""
printSleep('OPERATIONS ON STRINGS')

printSleep('ab' + 'cd' + 'concatenation')
printSleep(3 * 'ciao' + ' successive concatenation')
printSleep(len('ciao'))
printSleep('the length')
printSleep('ciao'[0] + ' indexing da 0 a length')
printSleep('ciao'[1])
printSleep('ciao'[2])
printSleep('ciao'[3])
printSleep('ciao'[1:3] + ' slicing ')
x = 1
printSleep(x)
x_str = str(x)
printSleep("my fav num is", x, ".", "x =", x)
printSleep("my fav num is " + x_str + ". " + "x = " + x_str)
# import numpy
# import matplotlib
aa = 'helloworld'
print(aa[1:9:2])
print(aa[::-1])
print(aa[-1])
print(aa[:-1])


def f(x):
    return 3


printSleep(f)  # richiama la funzione


def Square(x):
    return SquareHelper(abs(x), abs(x))


def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n - 1, x) + x


c = Square(3)
print(c)
stuff = ("iBoy", "iGirl", "iQ", "iC", "iPaid", "iPad")
for thing in stuff:
    if thing == 'iQ':
        printSleep("Found it")
