#Kevin McAdoo
#Purpose: Class assignment with if/else statements/ the use of and logical operators
#1-24-2018

#3. The and operator works as a logical operator for testing true/false statements
#where both statements have to be true or both statments have to be false

#4 The or operator works as another logical operator for testing true/false statements
#but this time one statement can be true and the other can be false

#5 The and operator

#7 Here you are asking the user to type in a random number between the following
random_number = int(input('Enter a number between 9 and 51: '))

#Here is a if command/ and logical operator for deciding if the input is valid
if random_number >= 9 and random_number <= 51:
    print('valid points')

#otherwise here is the command else when the input is not valid
else:
    print ('Invalid points')
