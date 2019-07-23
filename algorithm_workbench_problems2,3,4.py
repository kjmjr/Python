#Kevin McAdoo
#2-28-2018
#workbench 339-340 #2,3,4


#problem number 2
#you are opening the my_name.txt file for reading
infile = open('my_name.txt', 'r')

#reading the first line from the file
line1 = infile.readline()

#needed to close the file
infile.close()

print(line1)


#problem number 3
#open number_list file for writing
outfile = open('number_list.txt', 'w')

#a for loop to write a 100 numbers
for x in range(1, 101):
    outfile.write(str(x) + '\n')
    
#file is closed
outfile.close()

print ('Numbers have been written to number_list')
#problem number 4
#file is opened for reading
infile = open('number_list.txt', 'r')

#making a while because the end of the list is not found
line = infile.readline()
while line != '':
    line = infile.readline()
    line = line.rstrip()

print (line)
#file is closed
outfile.close()





