from app import app
from flask import render_template,request
from Todo import *
from flask import jsonify
from datetime import datetime
import os
import nltk
import random
@app.route('/gettitle')
def gettitle():
    file = open("perfume_box_titles.txt","r+")
    titles = file.readlines()
    title = "end"
    for i in range(0,len(titles),1):
        if titles[i].startswith("#"):
            continue
        title = titles[i].strip('\n')
        titles[i] = "#" + title + '\n'
        print title
        break

    f = open('perfume_box_titles.txt', 'w+')
    f.writelines(titles)
    f.close()
    file.close()
    return jsonify(title=title,
            keyword1=getkeyword(title),
            keyword2=getkeyword(title),
            keyword3=getkeyword(title))


def getkeyword(title):
    tokens = nltk.word_tokenize(title)
    index1 = random.randint(0, len(tokens))
    if index1==len(tokens):
        index1=index1-1
    index2 = random.randint(0, len(tokens))
    if index2==len(tokens):
        index2=index2-1
    index3 = random.randint(0, len(tokens))
    if index3 == len(tokens):
        index3 = index3 - 1
    print str(index1) + "  " + str(index2) + "  " + str(index3)
    print tokens[index1] + " " + tokens[index2] + " " + tokens[index3]
    return tokens[index1] + " " + tokens[index2] + " " + tokens[index3]

#===============================================================================================================================