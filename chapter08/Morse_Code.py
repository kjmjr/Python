#!:E:\py folder\chapter08\Morse_Code.py(3.63)

#Kevin McAdoo
#3-22-2018
#Morse Code homework



#asking for user to input a string 
string = input('Enter a sentence: ')

print('Your sentence is ', string)
print('Your sentence will convert to morse code \n' + 'Here it is: ')


#are dictionary is stored in this variable
MorseCodeDictionary = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': ' ....',
                       'i': '..', 'j': '.---', 'k': '-.-', 'l': ' .-..', 'm': ' --', 'n': ' -.', 'o': '---', 'p': '.--.',
                       'q': '--.-', 'r': '.-.', 's': '...', 't': ' -', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
                       'z': '--..', '0': ' -----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                       '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                       '.': '.-.-.-', ',': '--..--', '?': '..--..'}

#making a loop for the string
for line in string:
     #striping the string
     line = line.rstrip()
     #spliting each letter in the string
     string = line.rsplit()

#using an if statement to see if that letter is in the string print out its morse code in the dictionary below
     if 'a' in string:
     #the program runs a loop for everytime that letter is found in the input the letters reference is printed
      letter = 'a'
      for letter in string:
          print (MorseCodeDictionary['a'])
          print()
        

     elif 'b' in string:
       letter = 'b'
       for letter in string:
         print (MorseCodeDictionary['b'])
         print()


     elif 'c' in string:
       letter = 'c'
       for letter in string:
         print (MorseCodeDictionary['c'])
         print()

     elif 'd' in string:
       letter = 'd'
       for letter in string:
         print (MorseCodeDictionary['d'])
         print()


     elif 'e' in string:
       letter = 'e'
       for letter in string:
         print (MorseCodeDictionary['e'])
         print()


     elif 'f' in string:
       letter = 'f'
       for letter in string:
         print (MorseCodeDictionary['f'])
         print()


     elif 'g' in string:
       letter = 'g'
       for letter in string:
         print (MorseCodeDictionary['g'])
         print()


     elif 'h' in string:
       letter = 'h'
       for letter in string:
         print (MorseCodeDictionary['h'])
         print()


     elif 'i' in string:
       letter = 'i'
       for letter in string:
         print (MorseCodeDictionary['i'])
         print()


     elif 'j' in string:
       letter = 'j'
       for letter in string:
         print (MorseCodeDictionary['j'])
         print()


     elif 'k' in string:
       letter = 'k'
       for letter in string:
         print (MorseCodeDictionary['k'])
         print()


     elif 'l' in string:
       letter = 'l'
       for letter in string:
         print (MorseCodeDictionary['l'])
         print()


     elif 'm' in string:
       letter = 'm'
       for letter in string:
         print (MorseCodeDictionary['m'])
         print()


     elif 'n' in string:
       letter = 'n'
       for letter in string:
        print (MorseCodeDictionary['n'])
        print()


     elif 'o' in string:
       letter = 'o'
       for letter in string:
         print (MorseCodeDictionary['o'])
         print()


     elif 'p' in string:
       letter = 'p'
       for letter in string:
         print (MorseCodeDictionary['p'])
         print()


     elif 'q' in string:
       letter = 'q'
       for letter in string:
         print (MorseCodeDictionary['q'])
         print()


     elif 'r' in string:
       letter = 'r'
       for letter in string:
         print (MorseCodeDictionary['r'])
         print()


     elif 's' in string:
       letter = 's'
       for letter in string:
         print (MorseCodeDictionary['s'])
         print()


     elif 't' in string:
       letter = 't'
       for letter in string:
        print (MorseCodeDictionary['t'])
        print()


     elif 'u' in string:
       letter = 'u'
       for letter in string:
        print (MorseCodeDictionary['u'])
        print()


     elif 'v' in string:
       letter = 'v'
       for letter in string:
         print (MorseCodeDictionary['v'])
         print()


     elif 'w' in string:
       letter = 'w'
       for letter in string:
         print (MorseCodeDictionary['w'])
         print()


     elif 'x' in string:
       letter = 'x'
       for letter in string:
         print (MorseCodeDictionary['x'])
         print()


     elif 'y' in string:
       letter = 'y'
       for letter in string:
         print (MorseCodeDictionary['y'])
         print()


     elif 'z' in string:
       letter = 'z'
       for letter in string:
         print (MorseCodeDictionary['z'])
         print()


     elif '0' in string:
       letter = '0'
       for letter in string:
         print (MorseCodeDictionary['0'])
         print()


     elif '1' in string:
       letter = '1'
       for letter in string:
         print (MorseCodeDictionary['1'])
         print()


     elif '2' in string:
       letter = '2'
       for letter in string:
         print (MorseCodeDictionary['2'])
         print()


     elif '3' in string:
       letter = '3'
       for letter in string:
         print (MorseCodeDictionary['3'])
         print()


     elif '4' in string:
       letter = '4'
       for letter in string:
         print (MorseCodeDictionary['4'])
         print()


     elif '5' in string:
       letter = '5'
       for letter in string:
         print (MorseCodeDictionary['5'])
         print()


     elif '6' in string:
       letter = '6'
       for letter in string:
         print (MorseCodeDictionary['6'])
         print()


     elif '7' in string:
       letter = '7'
       for letter in string:
         print (MorseCodeDictionary['7'])
         print()


     elif '8' in string:
       letter = '8'
       for letter in string:
        print (MorseCodeDictionary['8'])
        print()


     elif '9' in string:
       letter = '9'
       for letter in string:
        print (MorseCodeDictionary['9'])
        print()


     elif '.' in string:
       letter = '.'
       for letter in string:
        print (MorseCodeDictionary['.'])
        print()


     elif ',' in string:
       letter = ','
       for letter in string:
        print (MorseCodeDictionary[','])
        print()


     elif '?' in string:
       letter = '?'
       for letter in string:
         print (MorseCodeDictionary['?'])
         print()

     else:
           print (string, ' was not found in the MorseCodeDictionary ')
          




