#Kevin McAdoo
#practice with list and tuples

#example of a printed tuple can change it (mutable)
x = (23, 56, 78, 59, 30, 40)

print (x)
print ()


#can't change a list (inmutable)
x = [45, 78, 69, 50, 30, 20]

#using the insert function
print ('Before inserting 89: ')
print (x)
print ()
x.insert (1, 89)
print ()
print ('After inserting 89:')
print (x)
print ()

#example of using the remove function with the try and except valueerror statements as well 
names = ['kevin', 'joe', 'billy', 'rex']

print ('Here is your string: ')


print (names)

item = input('Which name do you want to take out? ')

try:
    names.remove(item)

    print ('Here is your new string: ')
    print (names)
    
except ValueError:
    
    print ('That is not found in the list. ')


#example of inserting a new name into the program in a ran for loop 5 times 
print ()
print ('What name would you like to insert into this list? ')


for new in range(5):
    new = input('Add a name ')

    try:
        names.insert(1, new)
        print ('Here is your new set of names: ')
        print (names)
        
    except ValueError:
        
        print ('Input invalid ')

    
#example of a sorted list 
print ()
print ('Original list: ', x)
x.sort()
print ('Sorted list: ', x)


#example of a sorted list of names 
print ()
print ('Orignal set of names: ', names)
names.sort()
print ('New set of names', names)
