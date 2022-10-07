from flask import Flask, render_template, request, url_for, redirect, flash
import boto3
import json

aws_access_key_id = 'AKIA2NQPUTQ5BYTC7NS6'
aws_secret_access_key = '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'


app = Flask(__name__)

client = boto3.client('cloudtrail')

# pagi = client.get_paginator(lookup_events())

look = client.lookup_events()
data = []
type = []
time = []

@app.route("/")
def start():
    return render_template('index.html')

@app.route("/main", methods=["GET", "POST"])
def initialize():
    if request.method == 'POST':
        t = request.form['type']
        if not type:
            flash("Type is required!")
        else:
            data.clear()
            for x in range (50):
                data.append(look["Events"][x][t])
                time.append(look["Events"][x]["EventTime"])

    return render_template('main.html', data=data, len=len(data), type=type, time=time)

if __name__ == "__main__":
    app.run(debug=True)