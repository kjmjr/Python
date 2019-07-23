#The get_login_name function accepts a first name,
#last name, and ID number as arguments. It returns
#a system login name

def get_login_name(first,last,idnumber):
    #Get the first three letters of the first name
    #If the name is less than 3 characters, the
    #slice will return the entire first name
    set1 = first[0 : 3]

    #Get the first three letters of the last name
    #If the name is less than 3 characters, the
    #slice will return the entire ID number
    set3 = idnumber[-3 :]

    #put the sets of characters together
    login_name = set1 + set2 + set3

    #return the login name
    return login_name


#The valid_password function accepts a password as
#an argument and returns either true or false to
#indicate whether the password is valid. A valid
#password must be at least 7 characters in lenght,
#have at least one upperscase letter, one lowercase
#letter, and one digit

def valid_password(password):
    #set the boolean variables to false
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

#begin the validation. Start by testing the
#password's length.

    
    if len(password) >= 7:
      correct_length = True

      #Test each character and set the
      #appropriate flag when a required
      #character is found
      for ch in password:
          if ch.isupper():
              has_uppercase = True
          if ch.lower():
              has_lowercase = True
          if ch.isdigit():
              has_digit = True


    #Determine whether all of the requirments
    #are met. If they are, set is_valid to true.
    #otherwise, set is_valid to false.
    if correcct_length and has_uppercase and \
       has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    #return the is_valid variable
        return is_valid
