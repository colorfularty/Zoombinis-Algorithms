import random

class Zoombini(object):
    hair_styles = ["spiky",
                   "bowl cut",
                   "bald tuft",
                   "ponytail",
                   "green hat"]
    eyes_styles = ["normal",
                   "sleepy",
                   "cyclops",
                   "glasses",
                   "sunglasses"]
    nose_styles = ["orange",
                   "red",
                   "blue",
                   "green",
                   "purple"]
    feet_styles = ["pink shoes",
                   "spring",
                   "bicycle",
                   "propeller",
                   "roller skates"]
    traits = [hair_styles, eyes_styles, nose_styles, feet_styles]
    traitNames = ["hair", "eyes", "nose", "feet"]

    def __init__(self, hair, eyes, nose, feet):
        self.hair = hair
        self.eyes = eyes
        self.nose = nose
        self.feet = feet

    def __str__(self):
        return self.hair + " " + self.eyes + " " + self.nose + " " + self.feet

    @staticmethod
    def createGroup():
        result = []
        while len(result) < 16:
            z = Zoombini(random.choice(Zoombini.hair_styles),
                         random.choice(Zoombini.eyes_styles),
                         random.choice(Zoombini.nose_styles),
                         random.choice(Zoombini.feet_styles))
            if z not in result:
                result.append(z)
        return result

    @staticmethod
    def createGroupFromFile(fileName):
        group = []
        file = open(fileName + ".txt", 'r')
        for line in file:
            hair, eyes, nose, feet = line.split(":")
            if feet[-1] == '\n':
                feet = feet[:-1]
            group.append(Zoombini(hair, eyes, nose, feet))
        file.close()
        return group

    @staticmethod
    def getTraitCounts(group):
        counts = {}
        for trait in Zoombini.traits:
            for style in trait:
                counts[style] = 0
        for z in group:
            counts[z.hair] += 1
            counts[z.eyes] += 1
            counts[z.nose] += 1
            counts[z.feet] += 1
        return counts

    @staticmethod
    def existsZoombiniWithTraits(group, trait1, trait2):
        for z in group:
            if z.hair == trait1 or z.eyes == trait1 or z.nose == trait1 or z.feet == trait1:
                if z.hair == trait2 or z.eyes == trait2 or z.nose == trait2 or z.feet == trait2:
                    return True
        return False
    
    @staticmethod
    def createGroupFromUserInput():
        group = []
        while len(group) < 16:
            hair = textChoice(('1', '2', '3', '4', '5'), "Select a hair style for Zoombini " + str(len(group) + 1) + " (1: Spiky, 2: Bowl Cut, 3: Bald Tuft, 4: Ponytail, 5: Green Hat) ")
            eyes = textChoice(('1', '2', '3', '4', '5'), "Select an eyes style for Zoombini " + str(len(group) + 1) + " (1: Normal, 2: Sleepy, 3: Cyclops, 4: Glasses, 5: Sunglasses) ")
            nose = textChoice(('1', '2', '3', '4', '5'), "Select a nose style for Zoombini " + str(len(group) + 1) + " (1: Orange, 2: Red, 3: Blue, 4: Green, 5: Purple) ")
            feet = textChoice(('1', '2', '3', '4', '5'), "Select a feet style for Zoombini " + str(len(group) + 1) + " (1: Pink Shoes, 2: Spring, 3: Bicycle, 4: Propeller, 5: Roller Skates) ")
            group.append(Zoombini(Zoombini.hair_styles[int(hair) - 1], Zoombini.eyes_styles[int(eyes) - 1], Zoombini.nose_styles[int(nose) - 1], Zoombini.feet_styles[int(feet) - 1]))
        return group

def textChoice(textDecisions, inputText, errorText = "Invalid choice; try again."):
    result = None
    while result not in textDecisions:
        result = input(inputText)
        if result not in textDecisions:
            print(errorText)
    return result
