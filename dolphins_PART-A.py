"""
    Program models dolphin populations such that it tracks the average number of dolphins over the span of 149 years with their standard deviation.  Starting with an initial
    population of four dolphins, the program checks their procreation eligibility and subsequent children and mates them such that they produce a calf that will later be able
    to procreate as well.  Over the span of 149 years, the program tracks the dolphin population's information for 10 trials and provides a graph of the dolphin population
    over 149 years.
    
    This program file corresponds to PART A of the project.
"""

import random
import numpy as np
import re
import urllib
import matplotlib.pyplot as plt
import os.path

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
if os.path.isfile(male_filenm) == True:
    ''
else:
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

def MarvinGaye(mdictionary, fdictionary, partner1, partner2, malegen, femalegen):
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
            child_name = malegen.next()
            while child_name in mdictionary or child_name in fdictionary:
                child_name = malegen.next()
            mdictionary[child_name] = Dolphins(child_name, child_sex, FemalePartner, MalePartner)
            partner1.refracperiod = 0
            partner2.refracperiod = 0
        else:
            child_name = femalegen.next()
            while child_name in mdictionary or child_name in fdictionary:
                child_name = femalegen.next()
            fdictionary[child_name] = Dolphins(child_name, child_sex, FemalePartner, MalePartner)
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

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

m_dolphins = []
f_dolphins = []
living = []             # Initialized to track number of living dolphins each year of each trial.

# for loop used to match length of list for dictionary tracking in the following for loop.
for i in range(10):
    m_dolphins.append('hola'+str(i))
    f_dolphins.append('hola'+str(i))
    living.append('hola'+str(i))

for trial in range(10):
    # Set male and female generator equal to namegen() with respective genders to make use of .next() inside function.
    malegenerator = namegen('M')
    femalegenerator = namegen('F')
    m_dolphins[trial] = {elder_dolphins[2]: Dolphins(elder_dolphins[2], 'M', 'June', 'Stoon'), elder_dolphins[3]: Dolphins(elder_dolphins[3], 'M', 'Jill', 'Skrill')}
    f_dolphins[trial] = {elder_dolphins[0]: Dolphins(elder_dolphins[0], 'F', 'Jen', 'Sven'), elder_dolphins[1]: Dolphins(elder_dolphins[1], 'F', 'Jan', 'Stan')}
    print 'Trial No.', trial+1
    years = 0
    deaths = []
    living[trial] = []
    while years < 150:
        m_keys = m_dolphins[trial].keys()
        f_keys = f_dolphins[trial].keys()
        for dolphin in m_keys:
            for partner in f_keys:
                cool = MarvinGaye(m_dolphins[trial], f_dolphins[trial], m_dolphins[trial][dolphin], f_dolphins[trial][partner], malegenerator, femalegenerator)
        for dead in m_keys:
            m_dolphins[trial][dead].agify()
            if m_dolphins[trial][dead].age >= m_dolphins[trial][dead].death:
                if dead not in deaths:
                    deaths.append(dead)
        for dead in f_keys:
            f_dolphins[trial][dead].agify()
            if f_dolphins[trial][dead].age >= f_dolphins[trial][dead].death:
                if dead not in deaths:
                    deaths.append(dead)
        m_keys2 = m_dolphins[trial].keys()
        f_keys2 = f_dolphins[trial].keys()
        living[trial].append(len(m_keys2) + len(f_keys2) - len(deaths))
        if years % 25 == 0:
            print "#"*50
            print "Entering year {:d} with {:d} dolphins, with {:d} breeding.".format(years, len(m_keys) + len(f_keys) - len(deaths), abs(len(m_keys2)+len(f_keys2) - len(m_keys)-len(f_keys)))
        if years == 100:
            print "At year {:d}, there are {:d} living dolphins.\nthere have been {:d} births, in total.".format(years, len(m_keys2) + len(f_keys2) - len(deaths), len(m_keys2) + len(f_keys2) - 4)
        if years == 149:
            print "#"*50
            print "At year {:d}, there are {:d} living dolphins.".format(years, len(m_keys2) + len(f_keys2) - len(deaths))
        years += 1
    print

avg_std = []
for i in range(150):
    avg_std.append((np.mean([j[i] for j in living]), np.std([j[i] for j in living])))
std_above = [i + j for i, j in avg_std]
std_below = [i - j for i, j in avg_std]
avg = [i[0] for i in avg_std]

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

# Plots the average number of dolphins over a timespan
x = np.arange(0, years, 1)
plt.title('Average Population and Standard Deviation from 10 Trials')
plt.plot(x, avg, 'r')
plt.xlabel('Years')
plt.ylabel('Number of Living Dolphins')
plt.fill_between(x, std_below, std_above)

plt.show()

