#!/usr/bin/python
# -*- coding: utf-8 -*-

'''21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.'''

print("#-21---------------------------#")

def twenty_one(num):

    mod = num % 2
    if mod > 0:
        return("This is an odd number.")
    else:
        return("This is an even number.")

print(twenty_one(10))
print(twenty_one(7))



print("#-22---------------------------#")

'''22. Write a Python program to count the number 4 in a given list'''

def twenty_two(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(twenty_two([1, 4, 6, 7, 4]))
print(twenty_two([1, 4, 6, 4, 7, 4]))


print("#-23---------------------------#")

'''23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2'''

def twenty_three(str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)   #??????? жлолбити
    
    substr = str[:flen]

    result = ""
    
    for i in range(n):
        result = result + substr
    return (result)

print(twenty_three("verbatim", 5))
print(twenty_three("v", 5))



print("#-24---------------------------#")


'''24. Write a Python program to test whether a passed letter is a vowel or not. Go to the editor
'''

golosni = ['a', 'e', 'i', 'o', 'u']

def twenty_four(prugolosni):
    if prugolosni in golosni:
        print ('Це голосна !')
    else:
        print ('Це приголосна ! ')

print(twenty_four("s"))
print(twenty_four("a"))


print("#-25---------------------------#")


'''25. Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

'''


def twenty_five(group_nomer, n):
    
    for value in group_nomer:# цикл (value)  проходиться по group_nomer, з  умовою якщо цей прохід рівний 'n' тоді друкуємо щось там...
        if n == value:
            return True
    return False

    status = False 
    if n in group_nomer:
        status = True
    return status

print(twenty_five([1, 5, 8, 3], 3))
print(twenty_five([5, 8, 3], -1))



print("#-26---------------------------#")


'''26. Write a Python program to create a histogram from a given list of integers.'''

# взяти любий симол і пройшовшись по списку відобразити значенння  всіх цифрів

def twenty_six(items):
    for i in items:
        result = ""# чому якщо список винести за фор програма працює неадикватно????
        kilkis = i
        while(kilkis > 0):
            result += '*'
            kilkis = kilkis - 1
        print(result)

print(twenty_six([1,2,3,4,5,6,7,8,9]))






print("#-27---------------------------#")


'''27. Write a Python program to concatenate all elements in a list into a string and return it.'''

a_lst = [1,4,6,7,34,21,43,11,33]

result = ''
for i in (a_lst):
    result += str(i)

print(result)


print("#-28---------------------------#")
'''28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]'''


numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]



for i in numbers:
    if i == 237:
       print(i)
       break

    if i % 2 == 0:
        print(i) 
    


    
print("#-29---------------------------#")


'''29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
Test Data : 
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
Expected Output : 
{'Black', 'White'}'''

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

result = []


for color in color_list_1:
   if color not in color_list_2:
    result.append(color)

print(result)
    
'''color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

result = []


for color in color_list_1:
   if color not in color_list_2:
    das = result.append(color)

for color in color_list_2:
   if color not in color_list_1:
    das = result.append(color)
print(result)   приклад розвязання завдання з додаванням Green'''

print("#-30---------------------------#")

'''30. Write a Python program that will accept the base and height of a triangle and compute the area.'''


def thirty(b, h):
    
    area = b*h/2
    return(area)

print(thirty(10, 15))