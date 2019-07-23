#Kevin McAdoo
#Purpose: roman numeral printed output from the user
#1-24-2018

#user inputs a number between 1-10
number = int(input('Enter a number between 1 and 10: '))

#The boolean expression statement that tests if the users input is valid and prints the roman numerals
if (number >= 1 and number <= 10):
    print ('Roman Numeral Version of your input: ')

#This is printed if the users input is invalid else it continues with the following program
else:
    print ('ERROR')

 #Different roman numberal numbers that gets printed to whichever number is typed   
if number == 1:
    print ('Here: I')
elif number == 2:
    print ('Here: II')
elif number == 3:
    print ('Here: III')
elif number == 4:
    print ('Here: IV')
elif number == 5:
    print ('Here: V')
elif number == 6:
    print ('Here: VI')
elif number == 7:
    print ('Here: VII')
elif number == 8:
    print ('Here: VIII')
elif number == 9:
    print ('Here: IX')
elif number == 10:
    print ('Here: X')



    
