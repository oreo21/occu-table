from flask import Flask, render_template
from utils import occupation

app = Flask(__name__)
jobDict = occupation.genDictionary(scanCSV('data/occupations.csv'))

@app.route("/")
def root():
    return "Your shoes are untied."

@app.route("/occupations")
def occupationPage():
    jobRand = occupations.getRandOcc(jobDict)
    return render_template('occupations-template.html', jobCollection = jobDict, myJob = jobRand)

if __name__ == "__main__":
    app.debug = True
    app.run()
