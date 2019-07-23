#Kevin McAdoo
#2-21-2018
#Chapter 7 homework



#the set empty functions for is_prime = [] and non_prime = [] 
is_prime = []
non_prime = []

       
#2 for loops that are ran for non prime numbers
for rows in range(2):
    for cols in range (4):
        non_prime[rows][cols] = int(input('enter a number '))
        
    #x is the controlled variable
        for x in range(5):               
#if statement checks for validation to run through the program
         if (number % x) == 0 and number > 1:
            non_prime.append(number)  #the numbers taken are appended for non prime numbers
            print ('Non-Prime: ', non_prime)

           #x is the controlled variable 
            for x in range(5):
                #an if statement is ran if the number does not pass the first statement
                if (number % x ) != 0 and number > 1:
                    is_prime.append(number) #the numbers taken are appended for prime numbers
                    
               #for loop ran for prime numbers
                for rows in range(2):
                    for cols in range (4):
                        is_prime[rows][cols] = int(input('enter a number '))
                    print ('Prime: ', is_prime) #printed if it is a set of prime numbers
                        


