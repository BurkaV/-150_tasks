#!/usr/bin/python
# -*- coding: utf-8 -*-

'''31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. Go to the editor
Click me to see the sample solution

32. Write a Python program to get the least common multiple (LCM) of two positive integers. Go to the editor
Click me to see the sample solution'''


'''33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.'''
print("#-33---------------------------#")


def sum(a, b, c):
	if a == b or b == c or a == c:
		return("zero sum")

	else:
		sum = a + b + c
		return(sum)


print(sum(45, 2, 3))

print(sum(2, 2, 3))


print("#-34---------------------------#")
'''34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20'''

def sumer (one, two):
	sum = one + two
	if sum in range(15, 20): #  Дуже зручно із функціїю range яка вичесляє заданий діапозон
		return ('20')
	return (sum)
	
print(sumer(183, 1))
print(sumer(15, 1)) 

'''35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. '''

print("#-35---------------------------#")

def say_true (o, t):
	
	if o == t or o + t == 5 or o - t == 5:
		return True

	else:
		return False


print(say_true(183, 1))
print(say_true(1, 1))



'''36. Write a Python program to add two objects if both objects are an integer type.'''


print("#-36---------------------------#")

def add_int(a,  b):
	if not  (isinstance (a, int) and isinstance (b, int)):
		return("Erro")
	else:
		return (a + b)

print(add_int(12, 20))
print(add_int(12, 20.5))




'''37. Write a Python program to display your details like name, age, address in three different lines'''


print("#-37---------------------------#")

def twenty_seven():
	name = "Protos"
	age = "19"
	address = "Kiyv"
	print("Name: %s" % (name), "\nAge: %s"% (age), "\nAdrress: %s"% (address))

twenty_seven()

'''38. Write a Python program to solve (x + y) * (x + y). Go to the editor
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49'''
print("#-38---------------------------#")

def twenty_eight(a, b):
	result = (a + b) * (a + b)
	print("({} + {}) ^ 2) = {}".format(a, b, result))
	

twenty_eight(4, 3)






'''39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. Go to the editor
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79'''
'''Завдання скачав'''
print("#-39---------------------------#")
amt = 10000
int = 3.5
years = 7

future_value  = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))



'''40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). '''

'''Завдання скачав'''
print("#-39---------------------------#")
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)