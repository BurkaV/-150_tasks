
print("#11----------------------------#")
'''11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.'''
print(abs.__doc__)



print("#12----------------------------#")



'''12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. '''


import calendar

year= int(input('Enter the year: '))

month = int(input('Enter the month: '))

print(calendar.month(year, month))


print("#13----------------------------#")


'''13. Write a Python program to print the following here document. Go to the editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> exampl

#print("a string that you "don't" have to escape \n\tThis \nis a ....... multi-line \n heredoc string --------> example")
print(
'''



print("#14----------------------------#")

'''14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''
from datetime import date 
#enter = int(input("Enter deys: "))

data1 = date(2014, 7, 2)
data2 = date(2014, 7, 11)

pidsumku = data1 - data2

print(pidsumku)

print("#15----------------------------#")

'''15. Write a Python program to get the volume of a sphere with radius 6.'''

pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)

'''V=4/3*π*R3 - formula'''


print("#16----------------------------#")



'''16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference'''


n = int(input("Enter the number: "))

if n <= 17:
	print("ramainder :" (17 - n))

else:
	print("ramainder * 2: ", (n -17) * 2)



print("#17----------------------------#")


'''17. Write a Python program to test whether a number is within 100 of 1000 or 2000.'''

n = int(input("Enter the number: "))

if n <= 100:
	print("number within 100: ")

elif n > 100 and n <=1000:
	print("number within 1000: ")

elif n > 1000 and n <= 2000:
	print("number within 2000: ")


else:
	print("number beyond")

print("#18----------------------------#")


'''18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum'''

x = int(input("Enter the number x: "))
y = int(input("Enter the number y: "))
z = int(input("Enter the number z: "))

suma = x + y + z


if x == y == z:
	theesum = suma * 3
	print(theesum)

else:
	print(suma)


print("#19----------------------------#")

'''19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged'''


x = str(input("Enter the str: "))

if x[:2]=='Is':
	print(x)
else:
	print("Is" + x)



print("#20----------------------------#")

'''20. Write a Python program to get a string which is n (non-negative integer) copies of a given string'''

strr = str(input("Enter the str: "))
number= int(input("Enter the number : "))

result = ""


for i in range(number): #The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops.
    result = result + strr

print(result)


print("#----------------------------#")