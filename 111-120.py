'''111. Write a Python program to make file lists from current directory using a wildcard.'''

import glob
file_list = glob.glob('*.*')
print(file_list)



# Варіант вирішення, але Я цього не розумію....!!!





def one_hundred_twelve():
    
    num = [20, 30, 76, 105, 60, 450, 344]

    del num[0]
    
           
    print(num)

one_hundred_twelve()

'''Чому я не зміг передати - del num[0] перемінні і рездрукувати перемінну

	result = del num[0]
          
    print(result) '''



'''113. Write a Python program to input a number, if it is not a number generate an error message.'''


while True:

	try:

		a = int(input("Input a namber: "))
		break

	except ValueError:
		print("\nThis is not a number. Try again...")





'''114. Write a Python program to filter the positive numbers from a list.'''

x = [2, 3, -6, 65, 0, 54, -45, -65, 6, 3, 2]

result = []

def one_hundred_fourteen():
    for i in x:
        if i > 0:
            result.append(i)
       
    print(result)

one_hundred_fourteen()




'''115. Write a Python program to compute the product of a list of integers (without using for loop). '''



from functools import reduce

nums = [10, 20, 30, 40, 452]

def one_hundred_fifteen():
    nums_product = reduce( (lambda x, y: x * y), nums)
    print("Product of the numbers : ",nums_product)


one_hundred_fifteen()




'''116. Write a Python program to print Unicode characters.'''

# Не робив завдання, так я не знаю як його зробити....є варіант завдання 







'''117. Write a Python program to prove that two string variables of same value point same memory location.'''

mem = 'HelloWorld'


print('memory location: ', hex(id(mem)))

#Чому без id не працює????...



'''118. Write a Python program to create a bytearray from a list.'''

nums = [10, 20, 56, 35, 17, 99]

for x in nums: 
	print(x)


'''119. Write a Python program to display a floating number in specified numbers.'''


def one_hundred_nineteen():

	float_list = 532.1576452

	print(round(float_list, 1))
	print(round(float_list, 5))
	print(round(float_list, 2))


one_hundred_nineteen()


'''120. Write a Python program to format a specified string to limit the number of characters to 6.'''


def one_hundred_twenty():

	f_list = '5321576452'

	print('%.6s' % f_list)
	


one_hundred_twenty()
