#Defining and using the inventory class
#Kevin McAdoo
#4-22-2018


#importing the inventory module
from inventory import inventory
from product import product

def main():

  


   
#calling the inventory functions from the class
    inventory1 = inventory("1", "Jacket", "12", "$59.95")
    

    print (inventory1)
    print()
    

#the spacing on this constructor helps shape it when it is printed
#storing 4 arguments into the three variables
    
    Product1 = product(" 1   ", "Jacket ", "         12 ", "    $59.95 ")
    
    Product2 = product(" 2   ", "Designer Jeans ", " 40 ", "    $34.95 ")

    Product3 = product(" 3   ", "Shirt ", "          20 ", "    $24.95 ")

    print(" ID: " +  " Desription: " + "Quantity: " +  "Price: ")
    print(Product1)
    print()
    print(Product2)
    print()
    print(Product3)






main()
