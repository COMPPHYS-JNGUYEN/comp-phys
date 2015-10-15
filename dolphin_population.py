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
male_dir_path = "C:/Users/James/Documents/GitHub/comp-phys/"        # PC: "C:/Users/James/Documents/GitHub/comp-phys/"
male_filenm = male_dir_path + 'malenames.txt'                       # Mac: "/Users/labuser/comp-phys/"
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
while len(malenames) < 1000:    #Male Names Max: 7880
    x = maleurl.replace('1', str(i))
    xinfile = urllib.urlopen(x)
    xhtml = xinfile.readlines()
    xinfile.close()
    findnames(xhtml, 'M')
    i += 1

j = 1
while len(femalenames) < 1000:    # Female Names Max: 5974
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