#!/usr/bin/python
# -*- coding: utf-8 -*-


'''51. Write a Python program to determine profiling of Python programs. Go to the editor
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module. '''


import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')



'''52. Write a Python program to print to stderr.'''

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")


'''53. Write a python program to access environment variables. 
'''
# НЕ ЗРОЗУМІЛО ЩО ТАКЕ ЗМІННЕ СЕРЕДОВИЩЕ  environment variables???
import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')


'''54. Write a Python program to get the current username '''

# Returns the  current username!

import getpass
print(getpass.getuser())


'''55. Write a Python to find local IP addresses using Python's stdlib'''

# Returns the local IP 
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.connect(("8.8.8.8", 80))

print(s.getsockname()[0]) 
s.close()
# Returns the local IP 

'''56. Write a Python program to get height and width of the console window.'''

#returns height and width of the console window.


def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print('Number of columns and Rows: ',terminal_size())


'''57. Write a program to get execution time for a Python method.'''


import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))



'''58. Write a python program to sum of the first n positive integers.'''


n = 1, 2, 3, 4, 5, 6, 7, 8
s = 0
for i in n:
    s = s + i
print(s)

'''59. Write a Python program to convert height (in feet and inches) to centimeters.'''


def sum_sum (inches, feet):
    inches += feet * 12
    cam = round(inches * 2.54)
    print("Your height is : %d cm." % cam)

sum_sum(3, 5)



'''60. Write a Python program to calculate the hypotenuse of a right angled triangle.
'''



def prog_math(a,  b):
    from math import sqrt
    c = sqrt(a**2 + b**2)
    print("The length of the hypotenuse is", c )

prog_math(3, 4)