'''1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are'''


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

print("-.-.-.-.-.-.-.-.-.-.--.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-")





'''2. Write a Python program to get the Python version you are using. Go to the editor'''

import sys

print("Python version - ", sys.version)



print("-.-.-.-.-.-.-.-.-.-.--.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-")




'''3. Write a Python program to display the current date and time.
Sample Output : 
Current date and time : 
2014-07-05 14:34:14'''


import time
import datetime

print('time_1_ :', time.asctime())

print('time_2_ :', datetime.datetime.nowpython().strftime('%Y-%m-%d %H:%M:%S'))




print("-.-.-.-.-.-.-.-.-.-.--.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-")


'''4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output : 
r = 1.1
Area = 3.8013271108436504'''


import math

r = float(input("Enter the radius: "))

area = math.pi * r ** 2
print(area)

