import random

def scanCSV(CSVfile):   
    instream=open(CSVfile, 'r')
    content=instream.read().strip()
    instream.close()
    return content

def genDictionary(data):
    list1 = data.split("\n")
    list2 = []
    dict1 = {}
    del list1[0]
    del list1[-1]
    for x in list1:
        entry = x.rsplit(",", 2)
        entry[1] = float(entry[1])
        list2.append(entry)
    for a in list2:
        dict1[a[0]] = [a[1],a[2]]
    return dict1

def getRandOcc(occupations):
    occupationNames = []
    for data in occupations:
        for i in range(int(occupations[data][0] * 10)):
            occupationNames.insert(len(occupationNames), data)
    random.shuffle(occupationNames)
    return occupationNames[random.randint(0, len(occupationNames) - 1)]

#print getRandomOccupation(genDictionary(scanCSV("occupations.csv")))
#print scanCSV("occupations.csv")

