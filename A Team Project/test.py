from flask import Flask, redirect, url_for, render_template, request, flash
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

tempinput = [0]
cats = tempinput
print(cats)
whichcategory = int(random.choice(cats))
print(whichcategory)
question = get_quest(list(categories)[whichcategory])
print(str(question))
cate = (list(categories)[whichcategory])
print(cate)
question = list(cate.items())[question]
print(str(question))
quest, ans = question