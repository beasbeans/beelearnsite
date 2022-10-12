import json
from flask import Flask, redirect, url_for, render_template, request, flash, jsonify, make_response
from Dictionary_Builder import build_dict
from Get_Quests import get_quests, get_quest, textify
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
app.config['SECRET_KEY'] = 'They wIll neVer figUre out My supeR Cool seCret keY'
## app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


@app.route("/")
def home():
    return render_template("home.html")

cats = []
tempinput = []
@app.route("/quiz", methods=("GET","POST"))
def quiz():
    if request.method == 'POST':     
        global tempinput
        #if request.form.getlist('cats') != tempinput:
        if True:
            if tempinput != request.form.getlist('cats'):
                print("hello?")
                tempinput = request.form.getlist('cats')
            whichcategory = int(random.choice(tempinput))
            question = get_quest(list(categories)[whichcategory])
            cate = (list(categories)[whichcategory])
            question = list(cate.items())[question]
            global ans
            quest, ans = question
            if not tempinput:
                flash('Content is required!')
            else:
                return render_template("quiz.html", content=tempinput, question = quest, answer = ans)
    return render_template("quiz.html")

@app.route("/quiz/answer", methods=("GET","POST"))
def quizans():
    if request.is_json:
        global ans
        print(ans)
        answ = ans
        req = request.get_json()
        #print(req)
        receive = req['answer']
        #print(receive)
        response = {
        }



        def levenshteinDistance(s1, s2):
            if len(s1) > len(s2):
                s1, s2 = s2, s1

            distances = range(len(s1) + 1)
            for i2, c2 in enumerate(s2):
                distances_ = [i2+1]
                for i1, c1 in enumerate(s1):
                    if c1 == c2:
                        distances_.append(distances[i1])
                    else:
                        distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
            return distances[-1]
        print(levenshteinDistance(receive.lower(), answ.lower()))


        if receive.lower() in answ.lower() and receive.lower() != "" and receive.lower() != " ":
            response['accuracy'] = 'correct'
        else:
            print(answ)
            print(receive)
            response['accuracy'] = 'wrong'
        
        whichcategory = int(random.choice(tempinput))
        question = get_quest(list(categories)[whichcategory])
        cate = (list(categories)[whichcategory])
        question = list(cate.items())[question]
        quest, ans = question

        response['answer'] = ans
        response['question'] = quest

        res = make_response(jsonify(response))
        return res
    else:
        print('no json bby')
           
lightningquests = []
@app.route("/set")
def set():
    lightningquests = []
    i = 0
    for category in categories:
        categoriesquests[i] = get_quests(category)
        #print("\n\n\n\n" + str(categoriesquests[i]) + "\n\n\n\n\n")
        categoriesquests[i] = textify(category, categoriesquests[i])
        i += 1
    for l in range(0,20):
        print("\n\n\n\n\n\n" + str(l) + "\n\n")
        category = categories[random.randrange(0,(len(categories)-1))]
        lightningquests.append(get_quest(category))
        #print("\n\n\n\n" + str(categoriesquests[i]) + "\n\n\n\n\n")
        print("GAGAGAGGAGGGG                 " + str(lightningquests) + "          GAGGAGGAGAG")
        lightningquests[(l)] = textify(category, lightningquests[l])
    #print(list(categoriesquests[1])[1])
    return render_template("set.html", contentc=list(categoriesquests), contentl = list(lightningquests))

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port='8080', debug=False)
    app.run()


