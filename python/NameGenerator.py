#Kevin McAdoo
#3-6-2018
#Name Generator

#open the names.txt file for reading and storing it into names_file as a variable
names_file = open('names.txt', 'r')

#inializing the line as a variable
line = names_file.readline()

#a while loop for end of line not found
while line != '':

    #read the next line until end of marker is found
    line = names_file.readline()
    #print the next line
    print(line)
    
#close the names_file
names_file.close()

