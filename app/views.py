from app import app, models
from flask import render_template

@app.route('/')
def index():

    return render_template("home.html")

@app.route('/editor_horario')
def editor_horario():
    return(render_template('templates/editor_horario'))