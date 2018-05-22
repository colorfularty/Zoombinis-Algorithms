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

def textChoice(textDecisions, inputText, errorText = "Invalid choice; try again."):
    result = None
    while result not in textDecisions:
        result = input(inputText)
        if result not in textDecisions:
            print(errorText)
    return result
