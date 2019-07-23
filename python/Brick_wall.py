#Kevin McAdoo
#2-16-2018
#Brick wall homework assignment


#our define main function used in the program
def main():

      
#calling the get_integer() function
    width, height = get_integer()

       
#defining the get_integer function 
def get_integer():
   
#user enters a height and width as input
  height = int(input('Enter height:  '))
  width =  int(input('Enter width:  '))

#if statement for validation  
  if ( height > 2 and height < 10 and width > 2 and width < 10 ):
       print ('Brick wall:')

#print statements for underbar and vertical times the input that user types in  
       print (width * '_')
       
       print (height * '|')
       
       print (width * '_')
       
       print (height * '|')
       
       print (width * '_')

#else statement that shows when input is invalid       
  else:
      print ('invalid')
      
#returns width and height
  return width, height
  
 
#calling the main function
main()
