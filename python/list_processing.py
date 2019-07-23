#Kevin McAdoo
#2-21-2018
#Chapter 7 homework

print ('List of random numbers: ')
#list of random numbers
myList = [22, 47, 71, 25, 28, 61, 79, 57, 89, 3, 29, 41, 99, 86, 75, 98, 4, 31, 22, 33]

print (myList)

def main():

#command for the max function
    high = max(myList)
    print ('Highest number: ', high)
    
#command for the low function
    low = min(myList)
    print ('lowest number: ', low)
    
#command for the sum function
    total = sum(myList)
    print ('Sum: ', total)

#the acccumulator of the loop set
    final = 0.0
   
#a for loop is run get the values
    for value in myList:
         final += value
         
#command for the len function
    average = final/ len(myList)
    print ('Average: ', average)

#calling the main function
main()



