from flask import Flask, render_template, request, url_for, flash, redirect
from fetcher import all,specific_data
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

@app.route('/')
def index():
    return render_template('index.html',data=all())

if __name__ == "__main__":
    app.run(debug=True)
    