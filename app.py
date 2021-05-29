from flask import Flask, render_template, request, url_for, flash, redirect
from fetcher import all,specific_data
app = Flask(__name__)

@app.route('/country/<name>', methods=['GET','POST'])
def country(name):
    return render_template('country.html',data=specific_data(name))

@app.route('/country/',methods=['GET','POST'])
def enter():
    return render_template('enter_country.html',data=all())

@app.route('/')
def index():
    return render_template('index.html',data=all())

if __name__ == "__main__":
    app.run(debug=True)
    