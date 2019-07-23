''' Defining a book class
    Kevin McAdoo
    4-18-2018
'''



class Book:

    ''' Defining a book class that has the book's title, author's name, publisher's name'''


    def __init__(self, title,author,publisher):

        self.title = title
        self.author = author
        self.publisher = publisher



    def __str__(self):

        return "Title: " + self.title + "\n Author: " + self.author + "\n Publisher: " + self.publisher



'''  Unit Test '''
if __name__ == "__main__":
    book = Book("The Cat in the Hat", "Dr. Seuss", "Random House")
    print(book)
   

  

