#Margie Dietz
# 2/14/14
# While and For loops

def main():
    
 
    n = int (input ("How many bottles are there? "))
    print()

    for count in range (n,1,-1):   #range(start,end,interval)

          print (count, 'bottles of beer on the wall,')
          print (count, 'bottles of beer,')
          print ('Take one down, pass it around,')
          print (count-1, 'bottles of beer on the wall.')
          print ()
          #n = n - 1 

main()
