from Dictionary_Builder import build_dict
import random

amlit = build_dict("amlit.txt", "amlit", "amlit")
physsci = build_dict("physsci.txt", "physsci", "physsci")
amgov = build_dict("amgov.txt", "amgov", "amgov")
lifesci = build_dict("lifesci.txt", "lifesci", "lifesci")
finearts = build_dict("finearts.txt", "finearts", "finearts")
worldhist = build_dict("worldhist.txt", "worldhist", "worldhist")
amhist = build_dict("amhist.txt", "amhist", "amhist")
math = build_dict("math.txt", "math", "math")
geo = build_dict("geo.txt", "geo", "geo")
worldlit = build_dict("worldlit.txt", "worldlit", "worldlit")

def get_quests(category):
    questindices = []
    loc = random.randrange(0,(len(category)-1))
    tempquest = list(category.keys())[loc]
    #print(tempquest)
    split = tempquest.find(".")
    subcat = tempquest[:split]

    if loc >= 3:
        lowrange = loc - 3
    else:
        lowrange = 0
    if loc <= (len(category)-4):
        highrange = loc + 3
    else:
        highrange = (len(category)-1)

    for i in range(lowrange, highrange):
        testquest = list(category.keys())[i]
        if testquest[:split] == subcat:
            #print(i)
            questindices.append(i)
    if len(questindices) > 3:
        #print(questindices)
        tempquestindices = questindices
        questindices = []
        #print(questindices)
        for i in tempquestindices:
            leftovers = tempquest[(split+1):]
            #print(leftovers)
            split2 = leftovers.find(".")
            split = split + split2
            subcat = tempquest[:split]
            #print(subcat)
            testquest = list(category.keys())[i]
            if testquest[:split] == subcat:
                questindices.append(i)
    elif len(questindices) < 3:
        lowrange = 0
        highrange = 0
        if loc >= 1:
            lowrange = loc - 1
        else:
            lowrange = 0
            highrange += 1
        if loc <= (len(category)-2):
            highrange = highrange + loc + 1
        else:
            highrange = (len(category)-1)
            lowrange -= 1
        for i in range(lowrange,(highrange + 1)):
            questindices.append(i)

    return questindices
    #for i in questindices:
    #    print(list(category.keys())[i])

def textify(category, indices):
    questtuples = []
    for index in indices:
        questtuples.append(list(category.items())[index])
    return questtuples

#print(textify(amlit, [300,299,298]))
#print(len(amlit.keys()))
#print(list(amlit.keys())[0])
#print(question)
#print(answer)