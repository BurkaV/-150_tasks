#!/usr/bin/python
# -*- coding: utf-8 -*-



'''91. Write a Python program to swap two variables.'''

def ninety_one():
	a = 50
	b = 75
	print("a: %d"%a, "\nb: %d"%b)
	print()
	a,b = b,a
	print("a: %d"%a, "\nb: %d"%b)


ninety_one()



'''92. Write a Python program to define a string containing special characters in various forms.'''


'''
i don't understand it   
the task is not right'''


print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')

#Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,

'''93. Write a Python program to get the identity of an object'''

#identity of an object???


obj1 = object()
obj1_address = id(obj1)
print()
print(obj1_address)


#Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,

'''94. Write a Python program to convert a byte string to a list of integers.
'''

x = b'Abc'
print()
print(list(x))

#Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,


'''96. Write a Python program to print the current call stack.'''
'''


does not work

'''


def f1():
	return abc()

def abc():
    import traceback
    traceback.print_stack()


f1()


'''97. Write a Python program to list the special variables used within the language.'''


# Не зробив, зробити із Сашою



'''98. Write a Python program to get the system time. Go to the editor

Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.'''


import time

print(time.ctime())


'''99. Write a Python program to clear the screen or terminal.'''

import os
import time
# for windows
# os.system('cls')
os.system("ls")
time.sleep(2)
# Ubuntu version 10.10
os.system('clear')

'''100. Write a Python program to get the name of the host on which the routine is running.'''



import socket
host_name = socket.gethostname()

print("Host name:", host_name)
