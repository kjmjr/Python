#Kevin McAdoo
#1-31-2018
#Purpose: class practice

#here you are initializing for how many times the loop repeats
high = 10

#here you are making the total 0.0 digits places
total = 0.0

#the for loop command for entering a number
for count in range (high):
    number = int(input('Type in a number: '))
    total = total + number

#this command displays the total to the numbers entered
print ('The total is:', total)
