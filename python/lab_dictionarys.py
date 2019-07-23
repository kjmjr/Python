#Kevin McAdoo
#Purpose: Homework assignment finding unique words using a dictionary
#Cited: The counting word frequency using a dictionary video that strips the sentences in 2 files and checks if words are already in the
#dictionary or are new, also takes what word is used the most


#user can input file or press enter
fileName = input('Enter the file to search for or just press enter for simplicity: ' + '\n' + ' Repeat choice at the end of the program: ')

#this if statement is used for the user when they press enter
if len(fileName)< 1: fileName = ('ShortText.txt')

#opens the file
shortTextFile = open (fileName)

#dic is the created variable for the key word dict as the dictionary
dic = dict()

#this for loop breaks down every word in the line 
for line in shortTextFile:
    #line strips every word in the sentence
    line = line.rstrip()

    #line splits every word in the sentence
    words = line.split()


#running a for loop to check for unique words in the file
    for w in words:
        
    #the if statment checks for if the words already exist in the program ran by the for loop
        if w in dic:
            dic[w] = dic[w] + 1
            print (' (ALREADY EXIST) ')
            print()
     #else statment that checks for the words being new in the program and prints new word   
        else:
            dic[w] = 1
            print ('(NEW WORD) ')
            print()
        print (w, dic[w])

#prints the whole dictionary       
print (dic)
#creates a space everytime
print()

#variables that are initialized
large = -1
special = None

#this part of the prgrom runs a for loop for finding the word that is used the most out of the dictionary
for k,m in dic.items():
    if m > large:
        large = m
        special = k
print (special, 'is used the most in the dictionary: ',large)
print ()

#closes the file
shortTextFile.close()

#user can input file or press enter
bigFile = input('Enter the file to search for or just press enter for simplicity: ')

#this if statement is used for the user when they press enter
if len(bigFile)< 1: bigFile = ('GettysburgAddress.txt')

#opens the file
GBAFile = open (bigFile)

#dic is the created variable for the key word dict as out dictionary
dic = dict()

#this for loop runs a loop around every line in the file
for line in GBAFile:
    #this part strips the line
    line = line.rstrip()

    #this part splits the line
    words = line.split()
    

#running a for loop to check for unique words in the file
    for w in words:
        
    #the if statment checks for if the words exist in the program ran by the for loop
        if w in dic:
            dic[w] = dic[w] + 1
            print ('(ALREADY EXIST)')
            print()
            
     #else statment that checks for the words being new in the program and prints new word   
        else:
            dic[w] = 1
            print ('(NEW WORD)')
            print()
        print (w, dic[w])


print (dic)
print()

#variables that are initialized
large = -1
#none is a key word used in the program
special = None

#this part of the prgrom runs a for loop for finding the word that is used the most out of the dictionary
for g,a in dic.items():
    if a > large:
        large = a
        special = g
print (special, 'is used the most in the dictionary: ',large)
print ()

#closes the file
GBAFile.close()


