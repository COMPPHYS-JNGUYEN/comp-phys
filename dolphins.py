import random
import numpy

names = ['Charmander', 'Squirtle', 'Bulbasaur', 'Ekans', 'Diglet', 'Dodrio', 'Abra', 'Alakazam', 'Snorlax', 'Dugdrio', 'Chansey',\
         'Clefairy', 'Arbok', 'Charmelion', 'Wartortle', 'Ivysaur', 'Charizard', 'Blastoise', 'Pikachu', 'Raichu']

child_dict = {}

def MarvinGaye(partner1, partner2):
    if partner1.sex == 'M':
        MalePartner = partner1.name
    else:
        FemalePartner = partner1.name
    if partner2.sex == 'M':
        MalePartner = partner2.name
    else:
        FemalePartner = partner2.name
    if partner1.legal(partner2) == True:
        child_name = random.sample(names, 1)[0]
        child_dict[child_name] = Dolphins(child_name, random.sample(['M', 'F'], 1)[0], FemalePartner, MalePartner)
        names.remove(child_name)
        partner1.refracperiod = 0
        partner2.refracperiod = 0


class Dolphins:
    def __init__(self, name, sex, mother, father):
        self.name = name
        self.sex = sex
        self.age = 0
        self.mother = mother
        self.father = father
        self.death = random.gauss(35, 5)
        self.refracperiod = 0
    
    def agify(self):                                 ## Aging method: updates the age attribute each year.
        self.age += 1
        self.refracperiod += 1
    
    def legal(self, partner):                   ## Procreation method: determines whether a dolphin is allowed to procreate with another.
        if (self.age >= 8)\
        and (partner.age >= 8)\
        and (abs(self.age - partner.age) <= 10)\
        and (self.sex != partner.sex)\
        and (self.father != partner.father)\
        and (self.mother != partner.mother)\
        and (self.refracperiod > 5)\
        and (partner.refracperiod > 5):
            proc = True
        else:
            proc = False
        return proc


########################
##### Main Program #####
########################

elder_dolphins = ['Shakira', 'Jency', 'Lothar', 'JinBiao']
dolphinstances = {elder_dolphins[0]: Dolphins(elder_dolphins[0], 'F', 'Jen', 'Sven'),\
    elder_dolphins[1]: Dolphins(elder_dolphins[1], 'F', 'Jan', 'Stan'),\
    elder_dolphins[2]: Dolphins(elder_dolphins[2], 'M', 'June', 'Stoon'),\
    elder_dolphins[3]: Dolphins(elder_dolphins[3], 'M', 'Jill', 'Skrill')}