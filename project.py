from flask import Flask, render_template, redirect, url_for, request
import backend as back
import reminder

app = Flask(__name__)

user = "testing1"

@app.route('/')
@app.route('/home')
def home_page():
    # Get list of user readings from the database.
    user_readings = back.get_readings(user)
    return render_template('home.html', readings=user_readings)

@app.route('/add-goal', methods=['GET', 'POST'])
def goal_page():
    book_name = "Harry Potter"
    if request.method == 'POST':
        # Get all necessary data for adding a goal.
        goal_name = request.form.get("name", None)
        start_date = request.form.get("start_date", None)
        end_date = request.form.get("end_date", None)
        amount = request.form.get("amount", None)
        option = request.form.get("options", None)
        dates = request.form.getlist('date', None)
        print("Goal Name:", goal_name)
        print("Start Date:", start_date)
        print("End Date:", end_date)
        print("Amount:", amount)
        print("Option:", option)
        print("Dates:", dates)
        print(back.get_reading(user, book_name))
        back.add_reading_goal(user, book_name, goal_name, start_date)
        return redirect(url_for('home_page'))
    return render_template('add-goal.html')

@app.route('/add-reading', methods=['GET', 'POST'])
def add_page():
    if request.method == 'POST':
        # Get all necessary data for adding a reading.
        name = request.form.get("name", None)
        pages = request.form.get("pages", None)
        chapter = request.form.get("chapter", None)
        tags = request.form.get("tags", None)
        # Add the reading to the database.
        back.add_reading(user, name, pages, chapter, None, None)
        return redirect(url_for('home_page'))
    return render_template('add-reading.html')

@app.route('/edit-reading', methods=['GET', 'POST'])
def edit_page():
    if request.method == 'POST':
        # Get all necessary data for editing a reading.
        name = request.form.get("name", None)
        pages = request.form.get("pages", None)
        chapter = request.form.get("chapter", None)
        tags = request.form.get("tags", None)
        print("Name:", name)
        print("Pages:", pages)
        print("Chapter", chapter)
        print("Tags:", tags)
        print(back.get_reading(user, name))
        back.update_reading(user, name, pages, chapter)
    return render_template('edit-reading.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings_page():
    if request.method == 'POST':
        setting = request.form.get("setting", None)
        times = request.form.get("num_times", None)
        frequency = request.form.get("frequency", None)
        print(setting)
        print(times)
        print(frequency)
    return render_template('settings.html')
