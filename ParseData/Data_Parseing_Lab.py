#!:C:\Program files (x86)\Python36-32\Python.exe
#Command prompt
#Kevin Mcadoo
#Date: 4-17-2018
#Purpose: Data Parseing Lab


#opening a file of big data
infile = open('Big Data.txt', 'r')


records = []

#initializing variables to keep a running total for min and max values in the file
smallestNum = 0
largestNum = 0

#running a loop through the whole txt file
for records in infile:


#spliting the line we dont need
    print (records.split('-')[0])

#converting the string to an int to compare in the for loop   
    if smallestNum <= int(records):

        smallestNum++

    if largestNum >= int(records):

        largestNum++                 
                          

    

#closing infile
infile.close()     

print("The smallest set of data in Raleigh ever is ", smallestNum)
print("The largest set of data in Raleigh ever is ", largestNum)


  

 

            

                


          


