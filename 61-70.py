 """Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

   """





'''


61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.'''


def sixty_one(d_ft):
    d_inches = d_ft * 12
    d_yards = d_ft / 3.0
    d_miles = d_ft / 5280.0

    print("The distance in inches is %i inches." % d_inches)
    print("The distance in yards is %.2f yards." % d_yards)
    print("The distance in miles is %.2f miles." % d_miles)

sixty_one(100) 


'''62. Write a Python program to convert all units of time into seconds.'''



def sixty_two(days, hours, minutes, seconds):

    days = days * 3600 * 24
    hours = hours * 3600
    minutes = minutes * 60

    time = days + hours + minutes + seconds

    print("The  amounts of seconds", time)

sixty_two(5, 12, 45, 35) # converts all units of time into seconds


'''63. Write a Python program to get an absolute file path.'''



def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("5-10.py"))






'''64. Write a Python program to get file creation and modification date/times.'''

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("1-4.py")))
print("Created: %s" % time.ctime(os.path.getctime("1-4.py")))


'''65. Write a Python program to convert seconds to day, hour, minutes and seconds.'''


def sixty_five(time): 
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

sixty_five(14661112)




'''66. Write a Python program to calculate body mass index.'''

def sixty_six(height, weight):
	
	body = round(weight / (height * height), 2)

	print("Your body mass index is: %s" %(body))

sixty_six(5.8, 85)



'''67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.'''

'''
kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))

'''
'''68. Write a Python program to calculate the sum of the digits in an integer.'''



sum1 = '5245542'

result = 0


for i in sum1:

	int_test = int(i)

	result = result + int_test

print(result)



'''69. Write a Python program to sort three integers without using conditional statements and loops'''


x = 5

y = 2

z = 9

vse = x, y, z

print('Sort: ', sorted(vse))
print('Minimum:%s'% min(x, y , z))
print('Maxumum:%s' %max(x, y, z))


'''70. Write a Python program to sort files by date. '''

import glob
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))

