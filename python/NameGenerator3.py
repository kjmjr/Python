#Kevin McAdoo
#3-6-2018
#Name Generator part 3

def main():

    titles_file = "titles.txt"
    names_file = "name.txt"
    descriptor_file = "descriptor.txt"

    #displaying the function loadFile in def main function
    loadFile(titles_file, names_file, descriptor_file) 


def loadFile( titles_file, names_file, descriptor_file):

    
    #open the titles.txt file for reading and storing it into titles_file as a variable
    titles_file = open('titles.txt', 'r')
    
    #open the names.txt file for reading and storing it into names_file as a variable   
    names_file = open('names.txt', 'r')

    #open the descriptor.txt file for reading and storing it into descriptor_file as a variable
    descriptor_file = open('descriptor.txt', 'r')

    #inializing the line as a variable
    titles = titles_file.readline()

    #reading two lines from the file names.txt
    namesOne = names_file.readline()
    namesTwo = names_file.readline()

    #reading a line from the file descriptor.txt
    descriptor = descriptor_file.readline()

    
    #print the variable
    print( titles )
    print( namesOne )
    print( namesTwo )
    print the variable
    print('the', descriptor)


    #close the names_file
    titles_file.close()

     #close the names_file
    names_file.close()
    
    #close the names_file
    descriptor_file.close()


main()

