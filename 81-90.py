'''81. Write a Python program to concatenate N strings'''

def eighty_one():
	a = ' hello hellow '
	b = ' big boy '
	w = ' world super '

	concatenate = a + b + w
	print(concatenate)

eighty_one()

print()
def eighty_one_two():
	a = ['Im','super', 'programist', 'ura)', '!!!']
	

	concatenate = ' '.join(a)
	print(concatenate)

eighty_one_two()


'''82. Write a Python program to calculate the sum over a container.'''

print('Suma:', sum([20, 50, 200]))


'''83. Write a Python program to test whether all numbers of a list is greater than a certain number.'''


def eighty_three():
	number = [2, 4, 8]
	
	if [10] < number:
		print("True")

	else:
		print("Folse")


eighty_three()



'''84. Write a Python program to count the number occurrence of a specific character in a string. '''


s = "The quick brown fox jumps over the lazy dog."

print(s.count("o"))




'''85. Write a Python program to check if a file path is a file or a directory.'''

import os  
path="abc.txt"  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()



'''86.Write a Python program to get the ASCII value of a character.'''
def eighty_eight():
    print(ord('a'))
    print(ord('A'))
    print(ord('1'))
    print(ord('@'))

eighty_eight()



'''87. Write a Python program to get the size of a file.'''

import os
file_size = os.path.getsize("abc.txt")
print("\nThe size of abc.txt is :",file_size,"Bytes")


'''88. Given variables x=30 and y=20, write a Python program to print t "30+20=50".'''

def eighty_eight(x, y):
	print("\n%d+%d=%d" % (x, y, x+y))

eighty_eight(20, 30)



'''89. Write a Python program to perform an action if a condition is true. Go to the editor
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.'''


def eighty_nine(n):
	if n==1:
		print("n/First day of a Month!")

eighty_nine(1)



'''90. Write a Python program to create a copy of its own source code'''


print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())


#Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,Copy,