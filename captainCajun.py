from zoombini import *

ferry = []

def checkIfNeighbor(z1, z2):
    return z1.hair == z2.hair or z1.eyes == z2.eyes or z1.nose == z2.nose or z1.feet == z2.feet

def solveCaptainCajunsFerry(difficulty, group):
    global ferry
    ferry = []
    currentGroup = group[:]
    boardFerry(difficulty, currentGroup)

def boardFerry(difficulty, group):
    global ferry
    for i in range(len(group)):
        if checkNeighbors(difficulty, group, i):
            ferry.append(group[i])
            if len(ferry) == 16:
                return True
        else:
            continue
        newGroup = group[:]
        newGroup.remove(group[i])
        if boardFerry(difficulty, newGroup):
            return True
        ferry.remove(ferry[-1])
    return False

def checkNeighbors(difficulty, group, num):
    if difficulty == 1:
        if len(ferry) == 0:
            return True
        return checkIfNeighbor(ferry[-1], group[num])
    elif difficulty == 2:
        if len(ferry) == 0:
            return True
        elif len(ferry) < 8:
            return checkIfNeighbor(ferry[-1], group[num])
        elif len(ferry) == 8:
            return checkIfNeighbor(ferry[0], group[num])
        else:
            return checkIfNeighbor(ferry[-1], group[num]) and checkIfNeighbor(ferry[len(ferry) - 8], group[i])
    elif difficulty == 3:
        if len(ferry) == 0:
            return True
        elif len(ferry) < 4:
            return checkIfNeighbor(ferry[-1], group[num])
        elif len(ferry) % 4 == 0:
            return checkIfNeighbor(ferry[len(ferry) - 4], group[num])
        else:
            return checkIfNeighbor(ferry[len(ferry) - 4], group[num]) and checkIfNeighbor(ferry[-1], group[num])
    else:
        if len(ferry) == 0:
            return True
        elif len(ferry) < 4:
            return checkIfNeighbor(ferry[-1], group[num])
        elif len(ferry) == 4 or len(ferry) == 12:
            return checkIfNeighbor(ferry[len(ferry) - 4], group[num]) and checkIfNeighbor(ferry[len(ferry) - 3], group[num])
        elif len(ferry) < 7:
            return checkIfNeighbor(ferry[len(ferry) - 4], group[num]) and checkIfNeighbor(ferry[len(ferry) - 3], group[num]) and checkIfNeighbor(ferry[-1], group[num])
        elif len(ferry) == 7:
            return checkIfNeighbor(ferry[len(ferry) - 4], group[num]) and checkIfNeighbor(ferry[-1], group[num])
        elif len(ferry) == 8:
            return checkIfNeighbor(ferry[4], group[num])
        elif len(ferry) < 12:
            return checkIfNeighbor(ferry[len(ferry) - 4], group[num]) and checkIfNeighbor(ferry[len(ferry) - 5], group[num]) and checkIfNeighbor(ferry[-1], group[num])
        elif len(ferry) < 15:
            return checkIfNeighbor(ferry[len(ferry) - 4], group[num]) and checkIfNeighbor(ferry[len(ferry) - 3], group[num]) and checkIfNeighbor(ferry[-1], group[num])
        else:
            return checkIfNeighbor(ferry[len(ferry) - 4], group[num]) and checkIfNeighbor(ferry[-1], group[num])

difficulty = textChoice(('1', '2', '3', '4'), "What difficulty do you want to solve it on? (1-4) ")
decision = textChoice(('1', '2'), "Do you want to manually input each Zoombini here (1), or read them from a .txt file (2)? ")
if decision == '1':
    group = Zoombini.createGroupFromUserInput()
else:
    fileWorked = False
    while not fileWorked:
        filename = input("Enter the name of the .txt file with your Zoombini group (don't include .txt) ")
        try:
            group = Zoombini.createGroupFromFile(filename)
            fileWorked = True
        except Exception:
            print("No file exists with that name.")

solveCaptainCajunsFerry(int(difficulty), group)
for z in range(len(ferry)):
    print(str(z + 1) + ": " + str(ferry[z]))
