'''101Write a Python program to access and print a URL's content to the console.'''


from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)



'''102. Write a Python program to get system command output.'''

import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)



'''103. Write a Python program to extract the filename from a given path.'''

import os
print()
print(os.path.basename('/users/system1/student1/homework-1.py'))



'''104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.'''

# Зроробии із Сашою


 '''105. Write a Python program to get the users environment.'''

import os


print(os.environ)




'''106. Write a Python program to divide a path on the extension separator'''
# Зроробии із Сашою


'''107. Write a Python program to retrieve file properties.'''


import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__)


'''108. Write a Python program to find path refers to a file or directory when you encounter a path name.'''


import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))





'''109. Write a Python program to check if a number is positive, negative or zero'''

def one_hundred_nine(x):
	if x > 0:
		print("this is a positive number")

	elif x < 0:
		print("this is a negative number")

	elif x == 0:
		print("Zero")


one_hundred_nine(5)
one_hundred_nine(-58)
one_hundred_nine(0)




'''110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.'''

#!/usr/bin/python
# -*- coding: utf-8 -*-

def one_hundred_ten():
    
    num = 20, 30, 76, 105, 60, 450, 344
    s = ''
    for i in num:
        if i % 15==0:
            a = str(i)
            s = s + a
           
            print(a)

     


        
# не можу зробити щоб результат був  в один   ряд.... Доробити!!!
            



one_hundred_ten()


