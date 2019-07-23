''' Defining a product class
    Kevin McAdoo
    4-18-2018
'''
#the class product will be used for other programs
class product:

#the init method defines the variables
    def __init__(self, product_id, description, quantity, price):

        self.product_id = product_id
        self.description = description
        self.quantity = quantity
        self.price = price

    #the str method returns a string 
    def __str__(self):

        return self.product_id  + self.description  + self.quantity  + self.price


    
'''  Unit Test '''
if __name__ == "__main__":


#the spacing on this constructor helps shape it when it is printed
    Product1 = product(" 1   ", "Jacket ", "         12 ", "    $59.95 ")
    
    Product2 = product(" 2   ", "Designer Jeans ", " 40 ", "    $34.95 ")

    Product3 = product(" 3   ", "Shirt ", "          20 ", "    $24.95 ")

    print(" ID: " +  " Desription: " + "Quantity: " +  "Price: ")
    print(Product1)
    print()
    print(Product2)
    print()
    print(Product3)


    

    
   

  



