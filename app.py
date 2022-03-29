from flask import Flask, render_template, url_for, request
app = Flask(__name__)

database = {
    'user_first_names' : ['dylan'],
    'user_last_names' : ['barva']
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    print(request)
    first_name = request.form['fname']
    last_name = request.form['lname']
    if (first_name in database['user_first_names'] and last_name in database['user_last_names']):
        return {'login' : True, 'fname' : first_name, 'lname' : last_name }
    else:
        return {'login' : False}