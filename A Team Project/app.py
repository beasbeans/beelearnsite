from flask import Flask, redirect, url_for, render_template
from Dictionary_Builder import build_dict
from Get_Quests import get_quests, textify

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

amlitquests = []
physsciquests = []
amgovquests = []
lifesciquests = []
fineartsquests = []
worldhistquests = []
amhistquests = []
mathquests = []
geoquests = []
worldlitquests = []
    
categories = [amlit,physsci,amgov,lifesci,finearts,worldhist,amhist,math,geo,worldlit]
categoriesquests = [amlitquests,physsciquests,amgovquests,lifesciquests,fineartsquests,worldhistquests,amhistquests,mathquests,geoquests,worldlitquests]
app = Flask(__name__)

@app.route("/")
def tttt():
    return "<title> Hello! </title>"

@app.route("/set")
def set():
    i = 0
    for category in categories:
        categoriesquests[i] = get_quests(category)
        #print("\n\n\n\n" + str(categoriesquests[i]) + "\n\n\n\n\n")
        categoriesquests[i] = textify(category, categoriesquests[i])
        i += 1
    #print(list(categoriesquests[1])[1])
    return render_template("index.html", content=list(categoriesquests))


if __name__ == "__main__":
    app.run()

