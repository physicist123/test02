

print("hello")

l1 = [1,2,3]
print(l1)
# 1.1 自带package举例： os; os.getcwd();os.chdir(path)
import os
print(os.getcwd())

path = "d://software"
print(path)
path1 = os.chdir(path)
print(path1)

import math
print(math.sin(3.1415926/6))

from math import sin
print (sin(0.5))


# import numpy as np
# a= np.array((1,2,3))
# print(a)

a=100
b=100

c = "hello"
print(type(c))
print(id(a))
print(id(b))
print(id(100))

import sys
a = 5
b = 3

e = complex(a, b)
f = complex(float(a), float(b))

print ("a is type" , type(a))
print ("b is type" , type(b))
print ("e is type" , type(e))
print ("f is type" , type(f))

print(e)
print(e.real)

print(e.imag)
