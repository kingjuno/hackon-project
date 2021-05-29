from flask import Flask, render_template, request, url_for, flash, redirect
from fetcher import *
app = Flask(__name__)

@app.route('/country/<name>', methods=['GET','POST'])
def country(country):
    return render_template('country.html',data=specific_data(country))

@app.route('/country/',methods=['GET','POST'])
def enter():
    if request.method == 'POST':
        name = request.form['country']
        dta=specific_data(name)
        if dta[0]:
            return render_template('country.html',data=dta)
        else:
            return render_template('index.html',data=all())
    return render_template('enter_country.html')

@app.route('/info/', methods = ['GET','POST'])
def resource():
    city = request.form["n1"]
    required_resource = request.form["n2"]

    tweets = get_tweets(city, required_resource)
    if len(tweets) == 0:
        return render_template('error.html')
    else:    
        return render_template('resource_data.html', tweets = tweets)

@app.route('/resources/')
def resource_home():
    return render_template('resource.html')


@app.route('/')
def index():
    return render_template('index.html',data=all())

if __name__ == "__main__":
    app.run(debug=True)
    