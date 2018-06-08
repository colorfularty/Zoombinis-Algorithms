from zoombini import *

class Fleen(object):
    hair_styles = ["green spiky",
                   "purple mohawk",
                   "blue ponytail",
                   "red bandana",
                   "viking hair"]
    eyes_styles = ["triple",
                   "shifty",
                   "bandit mask",
                   "cyborg visor",
                   "red sunglasses"]
    nose_styles = ["black",
                   "orange",
                   "yellow",
                   "purple",
                   "cyan"]
    feet_styles = ["brown boots",
                   "red shoes",
                   "rockets",
                   "wheels",
                   "tank treads"]
    traits = [hair_styles, eyes_styles, nose_styles, feet_styles]

    def __init__(self, hair, eyes, nose, feet):
        self.hair = hair
        self.eyes = eyes
        self.nose = nose
        self.feet = feet

    @staticmethod
    def createGroup():
        result = []
        while len(result) < 16:
            f = Fleen(random.choice(Fleen.hair_styles),
                      random.choice(Fleen.eyes_styles),
                      random.choice(Fleen.nose_styles),
                      random.choice(Fleen.feet_styles))
            if f not in result:
                result.append(f)
        return result

    @staticmethod
    def createGroupFromFile(fileName):
        group = []
        file = open(fileName + ".txt", 'r')
        for line in file:
            hair, eyes, nose, feet = line.split(":")
            if feet[-1] == '\n':
                feet = feet[:-1]
            group.append(Fleen(hair, eyes, nose, feet))
        file.close()
        return group

    @staticmethod
    def getTraitCounts(group):
        counts = {}
        for trait in Fleen.traits:
            for style in trait:
                counts[style] = 0
        for f in group:
            counts[f.hair] += 1
            counts[f.eyes] += 1
            counts[f.nose] += 1
            counts[f.feet] += 1
        return counts

    @staticmethod
    def createGroupFromUserInput():
        group = []
        while len(group) < 16:
            hair = textChoice(('1', '2', '3', '4', '5'), "Select a hair style for Fleen " + str(len(group) + 1) + " (1: Green Spiky, 2: Purple Mohawk, 3: Blue Ponytail, 4: Red Bandana, 5: Viking Hair) ")
            eyes = textChoice(('1', '2', '3', '4', '5'), "Select an eyes style for Fleen " + str(len(group) + 1) + " (1: Triple, 2: Shifty, 3: Bandit Mask, 4: Cyborg Visor, 5: Red Sunglasses) ")
            nose = textChoice(('1', '2', '3', '4', '5'), "Select a nose style for Fleen " + str(len(group) + 1) + " (1: Black, 2: Orange, 3: Yellow, 4: Purple, 5: Cyan) ")
            feet = textChoice(('1', '2', '3', '4', '5'), "Select a feet style for Fleen " + str(len(group) + 1) + " (1: Brown Boots, 2: Red Shoes, 3: Rockets, 4: Wheels, 5: Tank Treads) ")
            group.append(Fleen(Fleen.hair_styles[int(hair) - 1], Fleen.eyes_styles[int(eyes) - 1], Fleen.nose_styles[int(nose) - 1], Fleen.feet_styles[int(feet) - 1]))
        return group

def solveFleens(zoombiniGroup, fleenGroup):
    zCounts = Zoombini.getTraitCounts(zoombiniGroup)
    fCounts = Fleen.getTraitCounts(fleenGroup)

    print(zCounts)
    print(fCounts)
    
    zHairStyleCounts = {}
    zEyesStyleCounts = {}
    zNoseStyleCounts = {}
    zFeetStyleCounts = {}
    fHairStyleCounts = {}
    fEyesStyleCounts = {}
    fNoseStyleCounts = {}
    fFeetStyleCounts = {}
    
    for style in zCounts:
        if style in Zoombini.hair_styles:
            zHairStyleCounts[style] = zCounts[style]
        if style in Zoombini.eyes_styles:
            zEyesStyleCounts[style] = zCounts[style]
        if style in Zoombini.nose_styles:
            zNoseStyleCounts[style] = zCounts[style]
        if style in Zoombini.feet_styles:
            zFeetStyleCounts[style] = zCounts[style]
            
    for style in fCounts:
        if style in Fleen.hair_styles:
            fHairStyleCounts[style] = fCounts[style]
        if style in Fleen.eyes_styles:
            fEyesStyleCounts[style] = fCounts[style]
        if style in Fleen.nose_styles:
            fNoseStyleCounts[style] = fCounts[style]
        if style in Fleen.feet_styles:
            fFeetStyleCounts[style] = fCounts[style]

    possibleTraitCorrelations = {}
    for trait1 in ("hair", "eyes", "nose", "feet"):
        for trait2 in ("hair", "eyes", "nose", "feet"):
            possibleTraitCorrelations[trait1, trait2] = True

    if sorted(fHairStyleCounts.values()) != sorted(zHairStyleCounts.values()):
        possibleTraitCorrelations["hair", "hair"] = False
    if sorted(fHairStyleCounts.values()) != sorted(zEyesStyleCounts.values()):
        possibleTraitCorrelations["eyes", "hair"] = False
    if sorted(fHairStyleCounts.values()) != sorted(zNoseStyleCounts.values()):
        possibleTraitCorrelations["nose", "hair"] = False
    if sorted(fHairStyleCounts.values()) != sorted(zFeetStyleCounts.values()):
        possibleTraitCorrelations["feet", "hair"] = False
        
    if sorted(fEyesStyleCounts.values()) != sorted(zHairStyleCounts.values()):
        possibleTraitCorrelations["hair", "eyes"] = False
    if sorted(fEyesStyleCounts.values()) != sorted(zEyesStyleCounts.values()):
        possibleTraitCorrelations["eyes", "eyes"] = False
    if sorted(fEyesStyleCounts.values()) != sorted(zNoseStyleCounts.values()):
        possibleTraitCorrelations["nose", "eyes"] = False
    if sorted(fEyesStyleCounts.values()) != sorted(zFeetStyleCounts.values()):
        possibleTraitCorrelations["feet", "eyes"] = False
        
    if sorted(fNoseStyleCounts.values()) != sorted(zHairStyleCounts.values()):
        possibleTraitCorrelations["hair", "nose"] = False
    if sorted(fNoseStyleCounts.values()) != sorted(zEyesStyleCounts.values()):
        possibleTraitCorrelations["eyes", "nose"] = False
    if sorted(fNoseStyleCounts.values()) != sorted(zNoseStyleCounts.values()):
        possibleTraitCorrelations["nose", "nose"] = False
    if sorted(fNoseStyleCounts.values()) != sorted(zFeetStyleCounts.values()):
        possibleTraitCorrelations["feet", "nose"] = False
        
    if sorted(fFeetStyleCounts.values()) != sorted(zHairStyleCounts.values()):
        possibleTraitCorrelations["hair", "feet"] = False
    if sorted(fFeetStyleCounts.values()) != sorted(zEyesStyleCounts.values()):
        possibleTraitCorrelations["eyes", "feet"] = False
    if sorted(fFeetStyleCounts.values()) != sorted(zNoseStyleCounts.values()):
        possibleTraitCorrelations["nose", "feet"] = False
    if sorted(fFeetStyleCounts.values()) != sorted(zFeetStyleCounts.values()):
        possibleTraitCorrelations["feet", "feet"] = False

    for key in possibleTraitCorrelations:
        if possibleTraitCorrelations[key]:
            print("Zoombini " + key[0] + " could correlate to Fleen " + key[1])

decision = textChoice(('1', '2'), "Do you want to manually input each Zoombini here (1), or read them from a .txt file (2)? ")
if decision == '1':
    zGroup = Zoombini.createGroupFromUserInput()
else:
    fileWorked = False
    while not fileWorked:
        filename = input("Enter the name of the .txt file with your Zoombini group (don't include .txt) ")
        try:
            zGroup = Zoombini.createGroupFromFile(filename)
            fileWorked = True
        except Exception:
            print("No file exists with that name.")
decision = textChoice(('1', '2'), "Do you want to manually input each Fleen here (1), or read them from a .txt file (2)? ")
if decision == '1':
    fGroup = Fleen.createGroupFromUserInput()
else:
    fileWorked = False
    while not fileWorked:
        filename = input("Enter the name of the .txt file with your Fleen group (don't include .txt) ")
        try:
            fGroup = Fleen.createGroupFromFile(filename)
            fileWorked = True
        except Exception:
            print("No file exists with that name.")
solveFleens(zGroup, fGroup)














    
