#Kevin McAdoo
#2-14-2018
#Test 1

#initializing that one kilometer is equal to 0.621 miles
one_kilo = 0.621

#the define main function is calling the def get_kilometers (): and def km_to_miles(): functions
def main():

#user inputs his number here and float means the number he/she uses does not have to be a whole number
    user_input = float(input('Enter a number: '))
    

        
    km_to_miles(user_input)     
    
    
#the def km_to_miles(): function
def km_to_miles(user_input):

    #the if statement for validating input  
    if user_input >= 0: 
      print ('One kilometer is equal to 0.621')
      print ('Your input was ', user_input)

    else:
        print ('Enter a positive number')

#math equation for calculating miles     
    miles = user_input * one_kilo
    print (user_input, 'is equal to', miles, 'miles')
#returns miles
    return miles
        
#calling main function
main()

    
