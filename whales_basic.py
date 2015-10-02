'''

The program instantiates various whale names into the class 'Whale' and randomly allocates a gender to the whale.
The program calculates the age of the whale upon request.
The program allows the whales to sing.


'''


import datetime as dt
import random


class Whale:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.born = dt.datetime.now()
        print 'A {:s} whale named {:s} is born!'.format(self.sex, self.name)
              
    def age(self):      # Calculates age of whale
        self.whaleage = dt.datetime.now() - self.born
        return self.whaleage
    
    def sing(self):     # Makes the whale sing
        return 5*'\a'
    
    def __str__(self):  # Prints name and age
        return 'A whale named {:s} (age {:s})'.format(self.name, self.age())

        
lst = ['Charmander', 'Squirtle', 'Bulbasaur', 'Ekans', 'Diglet', 'Dodrio', 'Abra', 'Alakazam', 'Snorlax', 'Dugdrio', 'Chansey', 'Clefairy', 'Arbok',\
      'Charmelion', 'Wartortle', 'Ivysaur', 'Charizard', 'Blastoise', 'Pikachu', 'Raichu']
instance = []
for i in lst:       # Instantiates all elements in lst and puts each instance into the empty list, instance.
    instance.append(Whale(i, random.sample(['male', 'female'], 1)[0]))

