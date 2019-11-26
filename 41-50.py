'''41. Write a Python program to check whether a file exists.'''
print("#-41---------------------------#")

def fourty_one():
	import os.path
	file = open('file.txt', 'w')
	print(os.path.isfile('file.txt'))
	print(os.path.isfile('berk.txt'))

fourty_one()


'''42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS'''

print("#-42---------------------------#")

import struct
print(struct.calcsize("P") * 8)



'''43. Write a Python program to get OS name, platform and release information'''

print("#-43---------------------------#")

import platform
import os
print(os.name)
print(platform.system())
print(platform.release())


'''44. Write a Python program to locate Python site-packages.'''

print("#-44---------------------------#")

import site; 
print(site.getsitepackages())


'''45. Write a python program to call an external command in Python.'''


print("#-45---------------------------#")

from subprocess import call
call(["ls", "-l"])

'''46. Write a python program to get the path and name of the file that is currently executing'''

print("#-46---------------------------#")

import os
print("Current File Name : ",os.path.realpath(__file__))


'''47. Write a Python program to find out the number of CPUs using'''

print("#-47---------------------------#")

import multiprocessing
print(multiprocessing.cpu_count())


'''48. Write a Python program to parse a string to Float or Integer.'''

print("#-48---------------------------#")

n = "246.2458"
print(float(n))
print(int(float(n)))


'''49. Write a Python program to list all files in a directory in Python.'''
print("#-49---------------------------#")


from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/bezil/Zavdany') if isfile(join('/home/students', f))]
print(files_list);


'''50. Write a Python program to print without newline or space.'''

print("#-50---------------------------#")

for i in range(0, 10):
    print('*', end="")
print("\n")