import random
import numpy
import re
import urllib
from pdb import set_trace

#####################################################################################################################

# malenames and femalenames initialized such that it extracts information from URLs and puts information into lists.
# Put above functions and other code to be used as global variable inside functions.
malenames = []
femalenames = []

# creates the text file directory path for the male and female lists for later extraction.
# put above functions and other code to be used as global variable inside functions.
male_dir_path = "C:/Users/James/Documents/GitHub/comp-phys/"         # PC: "C:/Users/James/Documents/GitHub/comp-phys/"
male_filenm = male_dir_path + 'malenames.txt'       # Mac: "/Users/labuser/comp-phys/"
female_dir_path = "C:/Users/James/Documents/GitHub/comp-phys/"
female_filenm = female_dir_path + 'femalenames.txt'

def findnames(code, gender):
    matchstring = 'nameDetails">.*</span>'
    if gender == 'M':
        namelist = []
        for item in code:
            x = re.findall(matchstring, item)
            if len(x) > 0:
                namelist.append(x[0])
        for stuff in namelist:
            new_stuff = stuff.lstrip('nameDetails">').rstrip('</span>')
            malenames.append(new_stuff)
    else:
        namelist = []
        for item in code:
            x = re.findall(matchstring, item)
            if len(x) > 0:
                namelist.append(x[0])
        for stuff in namelist:
            new_stuff = stuff.lstrip('nameDetails">').rstrip('</span>')
            femalenames.append(new_stuff)

def namegen(sex):
    x = 0
    y = 0
    if sex == 'M':
        with open(male_filenm,"r") as f:
            malenames = eval(f.read())
        while x < len(malenames)-1:
            yield malenames[x]
            x += 1
    else:
        with open(female_filenm, "r") as f:
            femalenames = eval(f.read())
        while y < len(femalenames):
            yield femalenames[y]
            y += 1

# Extracts male and female names from URL.
i = 1
maleurl = "http://www.prokerala.com/kids/baby-names/boy/page-1.html"
femaleurl = "http://www.prokerala.com/kids/baby-names/girl/page-1.html"
while len(malenames) < 7880:    #Male Names Max: 7880
    x = maleurl.replace('1', str(i))
    xinfile = urllib.urlopen(x)
    xhtml = xinfile.readlines()
    xinfile.close()
    findnames(xhtml, 'M')
    i += 1

j = 1
while len(femalenames) < 5974:    # Female Names Max: 5974
    y = femaleurl.replace('1', str(j))
    yinfile = urllib.urlopen(y)
    yhtml = yinfile.readlines()
    yinfile.close()
    findnames(yhtml, 'F')
    j += 1

# Make male and female names list extracted from websites text file that is writable.
with open(male_filenm, "w") as f:
    f.write(str(malenames))
with open(female_filenm, "w") as f:
    f.write(str(femalenames))

#####################################################################################################################
#####################################################################################################################

# Set male and female generator equal to namegen() with respective genders to make use of .next() inside function.
malegenerator = namegen('M')
femalegenerator = namegen('F')

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
        if child_sex == 'M':
            child_name = malegenerator.next()
            dolphinstances[child_name] = Dolphins(child_name, child_sex, FemalePartner, MalePartner)
            partner1.refracperiod = 0
            partner2.refracperiod = 0
        else:
            child_name = femalegenerator.next()
            dolphinstances[child_name] = Dolphins(child_name, child_sex, FemalePartner, MalePartner)
            partner1.refracperiod = 0
            partner2.refracperiod = 0
        return 1


class Dolphins:
    def __init__(self, name, sex, mother, father):
        self.name = name
        self.sex = sex
        self.age = 0
        self.mother = mother
        self.father = father
        self.death = random.gauss(35, 5)
        self.refracperiod = 0
    
## Aging method: updates the age attribute each year.
    def agify(self):
        self.age += 1
        self.refracperiod += 1

## Procreation method: determines whether a dolphin is allowed to procreate with another.
    def legal(self, partner):
        if (self.age >= 8)\
        and (partner.age >= 8)\
        and (abs(self.age - partner.age) <= 10)\
        and (self.sex != partner.sex)\
        and (self.father != partner.father)\
        and (self.mother != partner.mother)\
        and (self.refracperiod > 5)\
        and (partner.refracperiod > 5)\
        and (self.age <= self.death)\
        and (partner.age <= partner.death):
            proc = True
            return proc
        else:
            proc = False
            return proc

# Instantiate elder dolphins (with arbitrary parents).
elder_dolphins = ['Shakira', 'Jency', 'Lothar', 'JinBiao']
dolphinstances = {elder_dolphins[0]: Dolphins(elder_dolphins[0], 'F', 'Jen', 'Sven'),\
    elder_dolphins[1]: Dolphins(elder_dolphins[1], 'F', 'Jan', 'Stan'),\
    elder_dolphins[2]: Dolphins(elder_dolphins[2], 'M', 'June', 'Stoon'),\
    elder_dolphins[3]: Dolphins(elder_dolphins[3], 'M', 'Jill', 'Skrill')}

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

years = 0
deaths = []
while years < 150:
    temp1 = dolphinstances.keys()
    for dolphin in dolphinstances:
        dolphinstances[dolphin].agify()
    for dolphin in temp1:
        for partner in temp1:
            cool = MarvinGaye(dolphinstances[dolphin], dolphinstances[partner])
            if cool == 1:
                breeding += cool
    for elder in temp1:
        if dolphinstances[elder].age >= dolphinstances[elder].death:
            if elder not in deaths:
                deaths.append(elder)
#    set_trace()
    temp2 = dolphinstances.keys()
    if years % 25 == 0:
        print "#"*50
        print "Entering year {:d} with {:d} dolphins, with {:d} breeding.".format(years, len(temp1)-len(deaths), breeding)
    if years == 100:
        print "At year {:d}, there are {:d} living dolphins.\nthere have been {:d} births, in total.".format(years, len(temp2)-len(deaths), len(temp2)-4)
    if years == 149:
        print "#"*50
        print "At year {:d}, there are {:d} living dolphins.".format(years, len(temp2)-len(deaths))
    years += 1