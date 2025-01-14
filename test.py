import numpy as np
import sys

import random
print(random.randrange(1,3))

#comment here


"""   hiii
hiiii
hiiii"""
print(sys.version)
print(np.__version__)
print("hiii")
x = 4
y= 3.14
name = "ace"
lie = "false"

if x>y:
    print("x is greater")
else:
    print("y is greater")

for i in range(7):
      print(name)  
n = 5
while n > 0:
    print(n)
    n -= 1

def goodBye(n):
    return f" good bye {n}"    


print(goodBye(name))    
a,b,c = 1,2,3
print(a+b+c)
fruits = ["apple", "banana", "cherry"]
p, q, r = fruits
print(p)
print(q)
print(r)
print(p+ " "+q + " "+r)
print(p,q,r)

xy = "awesome"

def myfunc():
  xy = "fantastic"
  print("Python is " + xy)

myfunc()

print("Python is " + xy)
print(type(x),type(lie))

r = range(5)
print(r)
print(type(r))

h = b"Hello"
print(h,type(h))
for byte in h:
    print(byte)  # Outputs: 72 101 108 108 111

txt = "The best things in life are free!"
print("expensive" not in txt)
mlist = [1,2,3,4,5,6,7,8,9]
print(mlist)
for i in range(len(mlist)):
    
    print(mlist[i])
print(mlist[::-1])
print(mlist[2:7:2])