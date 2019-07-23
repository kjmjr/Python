
''' Defining a coin class
    Kevin McAdoo
    4-18-2018
'''

import random

class coin:

    ''' Defining a coin class that flips randomly
        self.side_up contains the showing side flip() flips the coin randomly'''

    def __init__(self):

        self.side_up = random.randint(1,2)

    def flip(self):

        self.side_up = random.randint(1,2)

    def __str__(self):

        if self.side_up == 1:

            return "Coins side shows heads"
        
        else:

            return "Coin side shows tails"
            

        
if __name__ == "__main__":

    '''' Unit Test '''

    coin1 = coin()
    coin2 = coin()
    


    for count in range(10):
        coin1.flip()
        coin2.flip()

        print(coin1)
        print(coin2)
        print('\n')

#this calls the comment at the top to print with the .__doc method
    print(coin1.__doc__)



        
