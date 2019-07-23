#Kevin McAdoo
#Test 2


#user can input file or press enter
infile = input('Enter the file to search for or just press enter for simplicity: ' + '\n' + ' Repeat choice at the end of the program: ')

#this if statement is used for the user when they press enter
if len(infile)< 1: infile = ('TestData1.txt')

#opens the file
infile = open('TestData1.txt', 'r')

#initialized
total = 0
#loop for run on total
for numbers in infile:

 amount = int(numbers)
 total += amount
 most = max(numbers)

infile.close()

mean = total/13

print ('Results: ')
print ('The mode is: ')
print(most)
print ('The mean is: ')
print(format(mean, ',.2f'))


#user can input file or press enter
infile = input('Enter the file to search for or just press enter for simplicity: ' + '\n' + ' Repeat choice at the end of the program: ')

#this if statement is used for the user when they press enter
if len(infile)< 1: infile = ('TestData2.txt')

#opens the file
infile = open ('TestData2.txt', 'r')

total = 0

for numbers in infile:

 amount = int(numbers)
 total += amount
 most = max(numbers)


infile.close()

mean = total/12

print ('Results: ')
print ('The mode is: ')
print(most)
print ('The mean is: ')
print(format(mean, ',.2f'))
