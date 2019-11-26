'''71. Write a Python program to get a directory listing, sorted by creation date.'''
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))


#Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy



''''72. Write a Python program to get the details of math module.'''

import math

math_details = dir(math)

print(math_details)


'''73. Write a Python program to calculate midpoints of a line'''

x1 = float(5)
y1 = float(9)

x2 = float(3)
y2 = float(5)

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print()
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print()


'''74. Write a Python program to hash a word.'''


soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
word=input("Input the word be hashed: ")
 
word=word.upper()
 
coded=word[0]
 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print() 
print("The coded word is: "+coded)
print()

#Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy


'''75. Write a Python program to get the copyright information.'''

import sys

print("\nPython Copyright Information")

print(sys.copyright)


'''76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script'''

import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

#Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy

'''77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.'''

import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()







'''78. Write a Python program to find the available built-in modules.'''



import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))


'''79. Write a Python program to get the size of an object in bytes.'''

import sys
str1 = "one"
str2 = "four"
str3 = "three"

print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")



'''80. Write a Python program to get the current value of the recursion limit.'''


import sys
print()
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
print()