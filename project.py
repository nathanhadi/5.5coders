from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

import backend
import reminder

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/goal')
def goal_page():
    return render_template('add-goal.html')

@app.route('/add-reading')
def add_page():
    return render_template('add-reading.html')

@app.route('/edit-reading')
def edit_page():
    return render_template('edit-reading.html')

@app.route('/settings')
def settings_page():
    return render_template('settings.html')