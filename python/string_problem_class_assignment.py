#Kevin McAdoo
#2-7-2018
#Purpose: class assignment that asks the user for a string then uses the string method to print the following in the program

#calling to the main function
def main():     
    string_problem()
    
    
#user inputs a sentence and it prints the input and is converted to uppercase and lowercase
def string_problem():
    string = input('Enter a sentence: ')
    stringOne = string.upper()    
    stringTwo = string.lower()
    print (string, stringOne, stringTwo )
#The string command that counts the length of the string entered
    str = ("Enter a sentence")
    print ("Length of the string you entered: ", len(str))

#end of calling to the main function
main()
