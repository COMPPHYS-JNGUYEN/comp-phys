class Dolphins():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.age = 0
        self.death = 0
        self.parents = []
        
    
    def MarvinGaye(self, partner):                   ## Procreation method: determines whether a dolphin is allowed to procreate with another.
        calf = 0
        if self.age >= 8 and abs(self.age - partner.age) <= 10 and self.sex != partner.sex:         ## Dolphin age 8 or greater; Within 10 years of mate; Opposite sex
            if self.parents == [] or partner.parents == [] or self.parents != partner.parents:      ## If elder dolphins, parents are non-existant, so empty list; If parents are the same, then 
                proc = True
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

