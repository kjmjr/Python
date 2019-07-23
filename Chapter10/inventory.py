''' Defining a inventory class
    Kevin McAdoo
    4-18-2018
'''

class inventory:

#sets the attributes with the __init__ method
    def __init__(self, product, description, quantity, price):

        self.product = product
        self.description = description
        self.quantity = quantity
        self.price1 = price

       
      
 #three__doc__strings is a method   
    def three__doc__strings(self):

        return  self.product, self.description, self.quantity, self.price

#the __str__ method returns a string of a sentence
    def __str__(self):

       return "Name: Kevin McAdoo " + "Date: 4-22-2018 "
       
    


'''  Unit Test '''
if __name__ == "__main__":


    inventory1 = inventory("1", "Jacket", "12", "$59.95")
    
    inventory2 = inventory("2", "Designer Jeans", "40", "$34.95")

    inventory3 = inventory("3", "Shirt", "20", "$24.95")

    
    print(inventory1)
    print()
    print(inventory2)
    print()
    print(inventory3)
   

    
  
    

               
