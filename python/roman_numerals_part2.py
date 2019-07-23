#Kevin McAdoo
#Purpose: roman numeral printed output from the user
#2-13-2018

#calling to main function command
def main():   

    number = int(input("Enter a number between 1 and 10: "))
    getInterger()
    print (number)

    RomanNumeral(romanNumber)
    
    
    
#call to getInteger function 
def getInterger():
    
    print ('Your input is: ')
    

#call to roman numeral number function 

def RomanNumeral(romanNumber):
  
#Different roman numberal numbers that gets printed to whichever number is typed using the if, elif and else statements  
    if romanNumber == 1:
            print ('Roman numeral version: I')
            
    elif romanNumber == 2:
            print ('Roman numeral version: II')
            
    elif romanNumber == 3:
            print ('Roman numeral version: III')
            
    elif romanNumber == 4:
            print ('Roman numeral version: IV')
            
    elif romanNumber == 5:
            print ('Roman numeral version: V')
            
    elif romanNumber == 6:
            print ('Roman numeral version: VI')
            
    elif romanNumber == 7:
            print ('Roman numeral version: VII')
            
    elif romanNumber == 8:
            print ('Roman numeral version: VIII')
            
    elif romanNumber == 9:
            print ('Roman numeral version: IX')
            
    elif romanNumber == 10:
            print ('Roman numeral version: X')
            
    else:
            print ('Error')  


#call the main function        
main()
