#Kevin McAdoo
#2-1-2018
#Purpose: List of prime numbers

#number is the variable for entering input
number = int(input('Enter a number and the computer will determine if it is prime: '))

#the for loop that tests if the input is prime
for x in range (2, number, x - 1):
  if (number % x != 0):
       print (number, end= ",")
       print ("is prime because it is only able to divide by 1 and itself")

#otherwise program skips to say input is not prime
  else:
      print (number, "is not prime")


