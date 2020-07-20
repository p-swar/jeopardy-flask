# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import requests 
import model
# -- Initialization section --
app = Flask(__name__)
## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    session["name"] = "Prachi"
    return render_template('index.html')
@app.route("/random")
def jeopardy_random():
    API_endpoint2="https://jservice.io/api/random"
    r=requests.get(API_endpoint2)
    data = r.json()
    return render_template("random_clue.html",data=data)
@app.route('/answerJeopardy', methods=['GET', 'POST'])
def answerJeopardy():
    if request.method=='GET':
        return ""
    else:
        model.display_clue(r)
#To access our API
# API_endpoint = "https://jservice.io/api/clues"
# API_query = "value=1000"
# API_url = API_endpoint +"?"+ API_query
# r = requests.get(API_url)
# data = r.json()
# print(API_url)












