from flask import Flask, render_template
import json
import pprint

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('demo-page.html')

if __name__=="__main__":
    app.run()
