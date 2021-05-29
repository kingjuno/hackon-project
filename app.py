from flask import Flask, render_template, request, url_for, flash, redirect
from fetcher import all
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',data=all())

if __name__ == "__main__":
    app.run(debug=True)