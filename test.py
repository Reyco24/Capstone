from ast import Str
from email.policy import default
from flask import Flask, render_template, request, url_for, redirect, flash
import boto3
import json

app = Flask(__name__)

client = boto3.client('cloudtrail',
region_name = 'us-east-1')

# pagi = client.get_paginator("lookup_events")
# pag = pagi.paginate

look = client.lookup_events()
data = []
time = []

#Idea to try: append to list within the data list, with amounts equal to whatever the page size should be
#length of operation can be entire length of data entries in dictionary

def finditem(t, dict):
    if t in dict.keys():
        return dict[t]
    else:
        for x in dict.keys():
            if type(dict[x]) is dict:
                finditem(t, dict[x])
            elif type(dict[x]) is list:
                for y in range (len(dict[x])):
                    if type(dict[x][y]) is dict:
                        finditem(t, dict[x][y])
            else:
                continue

@app.route("/main")
def start():
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def initialize():
    if request.method == 'POST':
        t = request.form['type']
        data.clear()
        for x in range (50):
            data.append(t)
            time.append(look["Events"][x]["EventTime"])

    return render_template('main.html', data=data, len=len(data), time=time, look=look)

# @app.route("/other", methods=["GET", "POST"])
# def initialize():
#     if request.method == 'POST':
#         t = request.form['type']
#         data.clear()
#     return render_template('other.html', data=data, len=len(data), type=type, time=time)


if __name__ == "__main__":
    app.run(debug=True)