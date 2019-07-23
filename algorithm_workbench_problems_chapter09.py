#Kevin McAdoo
#Algorithm workbench probems 1-4
#adding dictionarys

#problem 1 making a dictionary
alphabet = {'a' : '1', 'b' : '2', 'c' : '3'}

#problem 2 making a dictionary with a empty string
alphabet = {}

#problem 3 adding an if statment to print james assosiation if his name is found in the dictionary (this one finds him)
dct = {'James' : '336-239-9056', 'Sam' : '454-567-2393', 'Peter' : '919-232-4039'}

if 'James' in dct:
    print ('James has been found ')
    print ('James: ', dct['James'])
    print()

else:
    print ('Sorry James is not found ')

#problem 3 adding an if statement to print james assosiation if his name is found in the dictionary (this one does not find him)
dct = {'Sam' : '454-567-2393', 'Peter' : '919-232-4039'}

if 'James' in dct:
    print ('James: ', dct['James'])
    print()

else:
    print ('Sorry James is not found ')
    print()

#problem 4 that adds a del function
dct = {'James' : '336-239-9056', 'Sam' : '454-567-2393', 'Peter' : '919-232-4039', 'Jim' : '336-568-6955'}
 
if 'Jim' in dct:
    
#if jim is found in the dictionary the del function deletes his name and association from the dictionary
    del dct['Jim']
    print ('Jim and his assosiation has been deleted from the dictionary ')
    print()
    print ('New set Dictionary: ')
    print (dct)
    print()

else:
    print ('Sorry Jim is not deleted')
    print()
