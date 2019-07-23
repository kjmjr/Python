#Kevin McAdoo
#2-1-2018
#Purpose: Determine if user input is a prime number

#number is the variable for entering input
number = int(input('Enter a number and the computer will determine if it is prime: '))

#Here we are using an if statement with a nested for loop and if/ else statement to determine if the number is prime or not
#prime numbers are determined in this form by a number only able to divide by 1 and itself
if number > 1:

    for x in range(2, number):
        if (number % x ) == 0:
             print (number, 'is not a prime number')
             break
             
    else:
        print (number, 'is a prime number because it is only able to divide by 1 and itself')
             
#if the user input is not greater than 1 then this will show             
else:
    print (number, 'is not a prime number')
