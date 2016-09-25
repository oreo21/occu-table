from flask import Flask, render_template
import random

app = Flask(__name__)

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

def getRandomOccupation(occupations):
    occupationNames = []
    for data in occupations:
        for i in range(int(occupations[data][0] * 10)):
            occupationNames.insert(len(occupationNames), data)
    random.shuffle(occupationNames)
    return occupationNames[random.randint(0, len(occupationNames) - 1)]

jobDict = genDictionary(scanCSV('occupations.csv'))
jobRand = getRandomOccupation(jobDict)

@app.route("/")
def whatever():
    return "This page isn't meant to be accessed!"

@app.route("/occupations")
def printJobs():
    return render_template('occupations-template.html', jobCollection = jobDict, myJob = jobRand)
        
if __name__ == "__main__":
    app.debug = True
    app.run()

#print getRandomOccupation(genDictionary(scanCSV("occupations.csv")))
#print scanCSV("occupations.csv")

