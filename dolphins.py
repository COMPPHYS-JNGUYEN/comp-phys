import random
import numpy
import re
import urllib

#####################################################################################################################

malenames = []
femalenames = []

def findmalenames(code):
    matchstring = 'nameDetails">.*</span>'
    namelist = []
    for item in code:
        x = re.findall(matchstring, item)
        if len(x) > 0:
            namelist.append(x[0])
    for stuff in namelist:
        new_stuff = stuff.replace('nameDetails">', "")
        newnew_stuff = new_stuff.replace('</span>', "")
        malenames.append(newnew_stuff)

def findfemalenames(code):
    matchstring = 'nameDetails">.*</span>'
    namelist = []
    for item in code:
        x = re.findall(matchstring, item)
        if len(x) > 0:
            namelist.append(x[0])
    for stuff in namelist:
        new_stuff = stuff.replace('nameDetails">', "")
        newnew_stuff = new_stuff.replace('</span>', "")
        femalenames.append(newnew_stuff)
        
def namegen(sex):
    x = 0
    y = 0
    if sex == 'M':
        with open(male_path,"r") as f:
            malenames = eval(f.read())
            print malenames
        while x < len(malenames)-1:
            yield malenames[x]
            x += 1
    else:
        with open(female_path, "r") as f:
            femalenames = eval(f.read())
        while y < len(femalenames):
            yield femalenames[y]
            y += 1


i = 1
maleurl = "http://www.prokerala.com/kids/baby-names/boy/page-1.html"
femaleurl = "http://www.prokerala.com/kids/baby-names/girl/page-1.html"
while len(malenames) < 7880:    #7880
    x = maleurl.replace('1', str(i))
    xinfile = urllib.urlopen(x)
    xhtml = xinfile.readlines()
    xinfile.close()
    findmalenames(xhtml)
    i += 1

j = 1
while len(femalenames) < 5974:    #5974
    y = femaleurl.replace('1', str(j))
    yinfile = urllib.urlopen(y)
    yhtml = yinfile.readlines()
    yinfile.close()
    findfemalenames(yhtml)
    j += 1
    
male_dir_path = "C:/Users/James/Documents/GitHub/comp-phys/"      # "/Users/labuser/comp-phys/" for mac
male_filenm = male_dir_path + 'malenames.txt'
with open(male_filenm, "w") as f:
    f.write(str(malenames))
    
female_dir_path = "C:/Users/James/Documents/GitHub/comp-phys/"    # "/Users/labuser/comp-phys/" for mac
female_filenm = female_dir_path + 'femalenames.txt'
with open(female_filenm, "w") as f:
    f.write(str(femalenames))
    
#####################################################################################################################

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
        child_sex = random.sample(['M', 'F'], 1)[0]
        child_name = namegen(child_sex)
        child_dict[child_name] = Dolphins(child_name, child, FemalePartner, MalePartner)
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