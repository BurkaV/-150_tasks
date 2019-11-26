'''5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.'''



first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Hello ", last_name, first_name, "! ;)")


print("#----------------------------#")

'''6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.'''


dani =  3, 5, 7, 23

print("List: ", list(dani))
print("Tuple: ", tuple(dani))


print("#----------------------------#")
'''7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java 
Output : java'''

filename = input("Enter the Filename: ")
d = filename.split('.') 
print(d[1])

print("#----------------------------#")


'''8. Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]'''

color_list = ["Red","Green","White" ,"Black"]
print("first color: %s"%  color_list[0])
print("last color: %s" % color_list[3])

print("#----------------------------#")

'''9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014'''

exam_st_date = (11, 12, 2014)

data = ('The examination will start from: ''%i / %i / %i ' % exam_st_date)
print(data)

print("#----------------------------#")


'''10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5 
Expected Result : 615'''



n = int(input("Enter the namber: "))

n1 = int(n)
n2 = int(n * 2)
n3 = int( n * 3)
print(n1+n2+n3)



print("#----------------------------#")




