class Dolphins():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.age = 0
        self.death = 0
        
    
    def MarvinGaye(self):                   ## Procreation method: determines whether a dolphin is allowed to procreate with another.
        
    
    def elderfy(self):                      ## Aging method: updates the age attribute each year.
        pass
    
    
########################
##### Main Program #####
########################

elder_dolphins = ['Shakira', 'Jency', 'Lothar', 'JinBiao']
dolphinstances = []
dolphinstances.append(Dolphins(elder_dolphins[0], 'F'))
dolphinstances.append(Dolphins(elder_dolphins[1], 'F'))
dolphinstances.append(Dolphins(elder_dolphins[2], 'M'))
dolphinstances.append(Dolphins(elder_dolphins[3], 'M'))

for i in dolphinstances:
    print i.name
    print i.sex
    print i.age
    print i.death