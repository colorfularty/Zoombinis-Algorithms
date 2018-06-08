from zoombini import *

def solveOnVeryHard(group, hotel):
    possible_solutions = {}
    counts = Zoombini.getTraitCounts(group)
    for rowTrait in Zoombini.traits:
        firstRowTraits = rowTrait[:]
        for firstRowTrait in firstRowTraits:
            #print("First row:", firstRowTrait)
            secondRowTraits = firstRowTraits[:]
            secondRowTraits.remove(firstRowTrait)
            for secondRowTrait in secondRowTraits:
                #print("Second row:", secondRowTrait)
                thirdRowTraits = secondRowTraits[:]
                thirdRowTraits.remove(secondRowTrait)
                for thirdRowTrait in thirdRowTraits:
                    #print("Third row:", thirdRowTrait)
                    fourthRowTraits = thirdRowTraits[:]
                    fourthRowTraits.remove(thirdRowTrait)
                    for fourthRowTrait in fourthRowTraits:
                        #print("Fourth row:", fourthRowTrait)
                        fifthRowTraits = fourthRowTraits[:]
                        fifthRowTraits.remove(fourthRowTrait)
                        fifthRowTrait = fifthRowTraits[0]
                        #print("Fifth row:", fifthRowTrait)
                        for colTrait in Zoombini.traits:
                            if rowTrait != colTrait:
                                firstColTraits = colTrait[:]
                                for firstColTrait in firstColTraits:
                                    #print("First col:", firstColTrait)
                                    try:
                                        if possible_solutions[Zoombini.traits.index(rowTrait), Zoombini.traits.index(colTrait)]:
                                            pass
                                    except KeyError:
                                        possible_solutions[Zoombini.traits.index(rowTrait), Zoombini.traits.index(colTrait)] = []
                                    if Zoombini.existsZoombiniWithTraits(group, firstRowTrait, firstColTrait) and not hotel[0][0]:
                                        #print("Problem in row 1 col 1")
                                        continue
                                    if Zoombini.existsZoombiniWithTraits(group, secondRowTrait, firstColTrait) and not hotel[1][0]:
                                        #print("Problem in row 2 col 1")
                                        continue
                                    if Zoombini.existsZoombiniWithTraits(group, thirdRowTrait, firstColTrait) and not hotel[2][0]:
                                        #print("Problem in row 3 col 1")
                                        continue
                                    if Zoombini.existsZoombiniWithTraits(group, fourthRowTrait, firstColTrait) and not hotel[3][0]:
                                        #print("Problem in row 4 col 1")
                                        continue
                                    if Zoombini.existsZoombiniWithTraits(group, fifthRowTrait, firstColTrait) and not hotel[4][0]:
                                        #print("Problem in row 5 col 1")
                                        continue
                                    secondColTraits = firstColTraits[:]
                                    secondColTraits.remove(firstColTrait)
                                    for secondColTrait in secondColTraits:
                                        #print("Second col:", secondColTrait)
                                        if Zoombini.existsZoombiniWithTraits(group, firstRowTrait, secondColTrait) and not hotel[0][1]:
                                            #print("Problem in row 1 col 2")
                                            continue
                                        if Zoombini.existsZoombiniWithTraits(group, secondRowTrait, secondColTrait) and not hotel[1][1]:
                                            #print("Problem in row 2 col 2")
                                            continue
                                        if Zoombini.existsZoombiniWithTraits(group, thirdRowTrait, secondColTrait) and not hotel[2][1]:
                                            #print("Problem in row 3 col 2")
                                            continue
                                        if Zoombini.existsZoombiniWithTraits(group, fourthRowTrait, secondColTrait) and not hotel[3][1]:
                                            #print("Problem in row 4 col 2")
                                            continue
                                        if Zoombini.existsZoombiniWithTraits(group, fifthRowTrait, secondColTrait) and not hotel[4][1]:
                                            #print("Problem in row 5 col 2")
                                            continue
                                        thirdColTraits = secondColTraits[:]
                                        thirdColTraits.remove(secondColTrait)
                                        for thirdColTrait in thirdColTraits:
                                            #print("Third col:", thirdColTrait)
                                            if Zoombini.existsZoombiniWithTraits(group, firstRowTrait, thirdColTrait) and not hotel[0][2]:
                                                #print("Problem in row 1 col 3")
                                                continue
                                            if Zoombini.existsZoombiniWithTraits(group, secondRowTrait, thirdColTrait) and not hotel[1][2]:
                                                #print("Problem in row 2 col 3")
                                                continue
                                            if Zoombini.existsZoombiniWithTraits(group, thirdRowTrait, thirdColTrait) and not hotel[2][2]:
                                                #print("Problem in row 3 col 3")
                                                continue
                                            if Zoombini.existsZoombiniWithTraits(group, fourthRowTrait, thirdColTrait) and not hotel[3][2]:
                                                #print("Problem in row 4 col 3")
                                                continue
                                            if Zoombini.existsZoombiniWithTraits(group, fifthRowTrait, thirdColTrait) and not hotel[4][2]:
                                                #print("Problem in row 5 col 3")
                                                continue
                                            fourthColTraits = thirdColTraits[:]
                                            fourthColTraits.remove(thirdColTrait)
                                            for fourthColTrait in fourthColTraits:
                                                #print("Fourth col:", fourthColTrait)
                                                if Zoombini.existsZoombiniWithTraits(group, firstRowTrait, fourthColTrait) and not hotel[0][3]:
                                                    #print("Problem in row 1 col 4")
                                                    continue
                                                if Zoombini.existsZoombiniWithTraits(group, secondRowTrait, fourthColTrait) and not hotel[1][3]:
                                                    #print("Problem in row 2 col 4")
                                                    continue
                                                if Zoombini.existsZoombiniWithTraits(group, thirdRowTrait, fourthColTrait) and not hotel[2][3]:
                                                    #print("Problem in row 3 col 4")
                                                    continue
                                                if Zoombini.existsZoombiniWithTraits(group, fourthRowTrait, fourthColTrait) and not hotel[3][3]:
                                                    #print("Problem in row 4 col 4")
                                                    continue
                                                if Zoombini.existsZoombiniWithTraits(group, fifthRowTrait, fourthColTrait) and not hotel[4][3]:
                                                    #print("Problem in row 5 col 4")
                                                    continue
                                                fifthColTraits = fourthColTraits[:]
                                                fifthColTraits.remove(fourthColTrait)
                                                fifthColTrait = fifthColTraits[0]
                                                #print("Fifth col:", fifthColTrait)
                                                if Zoombini.existsZoombiniWithTraits(group, firstRowTrait, fifthColTrait) and not hotel[0][4]:
                                                    #print("Problem in row 1 col 5")
                                                    continue
                                                if Zoombini.existsZoombiniWithTraits(group, secondRowTrait, fifthColTrait) and not hotel[1][4]:
                                                    #print("Problem in row 2 col 5")
                                                    continue
                                                if Zoombini.existsZoombiniWithTraits(group, thirdRowTrait, fifthColTrait) and not hotel[2][4]:
                                                    #print("Problem in row 3 col 5")
                                                    continue
                                                if Zoombini.existsZoombiniWithTraits(group, fourthRowTrait, fifthColTrait) and not hotel[3][4]:
                                                    #print("Problem in row 4 col 5")
                                                    continue
                                                if Zoombini.existsZoombiniWithTraits(group, fifthRowTrait, fifthColTrait) and not hotel[4][4]:
                                                    #print("Problem in row 5 col 5")
                                                    continue
                                                possible_solutions[Zoombini.traits.index(rowTrait), Zoombini.traits.index(colTrait)].append([[firstRowTrait,
                                                                                                                                             secondRowTrait,
                                                                                                                                             thirdRowTrait,
                                                                                                                                             fourthRowTrait,
                                                                                                                                             fifthRowTrait],
                                                                                                                                            [firstColTrait,
                                                                                                                                             secondColTrait,
                                                                                                                                             thirdColTrait,
                                                                                                                                             fourthColTrait,
                                                                                                                                             fifthColTrait]])
                                                
    return possible_solutions

def findSafeFirstMoves(hotel, solutions):
    possiblePositions = {}
    for i in range(5):
        for j in range(5):
            possibleZoombinis = []
            if hotel[i][j]:
                
            possiblePositions[(i, j)] = possibleZoombinis

group = Zoombini.createGroupFromFile("group4")
hotel = [[True , False, True , True , False],
       [True , True , False, True , True ],
       [True , False, True , False, True ],
       [True , True , True , True , True ],
       [False, True , True , False, False]]
solutions = solveOnVeryHard(group, hotel)
for solutionPair in solutions:
    print(solutionPair)
    for solution in solutions[solutionPair]:
        print('\t', solution[0])
        print('\t', solution[1])
