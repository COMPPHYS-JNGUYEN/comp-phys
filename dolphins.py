class Dolphins():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.age = 0
        self.mother =
        self.father =
        self.death = 0
        self.refracperiod = 0
    
    def MarvinGaye(self, partner):                   ## Procreation method: determines whether a dolphin is allowed to procreate with another.
        calf = 0
        if self.age >= 8 and abs(self.age - partner.age) <= 10 and self.sex != partner.sex and self.father != :         ## Dolphin age 8 or greater; Within 10 years of mate; Opposite sex
            
        else:
            proc = False
    
    def agify(self):                                 ## Aging method: updates the age attribute each year.
        self.age += 1
        return self.age
    
    
########################
##### Main Program #####
########################

elder_dolphins = ['Shakira', 'Jency', 'Lothar', 'JinBiao']
dolphinstances = []
dolphinstances.append(Dolphins(elder_dolphins[0], 'F'))
dolphinstances.append(Dolphins(elder_dolphins[1], 'F'))
dolphinstances.append(Dolphins(elder_dolphins[2], 'M'))
dolphinstances.append(Dolphins(elder_dolphins[3], 'M'))

