#!:C:/Users/Vaughan/Documents/commandLine/testLeapYear.bat(3.64)

#Kevin McAdoo
#Purpose: Determine if the year entered by the user is a leap year
#1-24-2018

#where  the user enters his input
leap_year = int(input('Enter a 4 digit year and the computer will determine if it is a leap year: '))


#if and else commands for determining if the users input is a leap year or not
if ((leap_year % 4) == 0):
    
    if ((leap_year % 100 ) == 0):

        if ((leap_year % 400) == 0):

            print ('The year:', leap_year, 'is a leap year')
            
        else:

            print('The year:', leap_year, 'is not a leap year')
            
    else:

        print('The year:', leap_year, 'is a leap year')
         

#one of the else statements that returns users output as not a leap year
else:

    print('The year:', leap_year, 'is not a leap year')
