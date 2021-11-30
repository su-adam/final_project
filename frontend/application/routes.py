from application import app
from application.forms import LocationForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "final_project-backend:5000"

# view galleries and location for homepage

@app.route('/')
@app.route('/home')
def home():
    all_locations = requests.get(f"http://{backend_host}/read/allLocation").json()
    app.logger.info(f"Locations: {all_locations}")
    return render_template('index.html', title="Home", all_locations=all_locations["locations"])

#create location /'update location'/
@app.route('/create/locations', methods=['GET','POST'])
def create_location():
    form = TaskForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/location",
            json = {"location" : form.location.data}
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_location.html", title="Select location from London", form=form)

#create galleries /update galleries / delete galleries

@app.route('/update/task/<int:id>', methods=['GET','POST'])
def update_task(id):
    form = TaskForm()
    task = requests.get(f"http://{backend_host}/read/task{id}").json()
    app.logger.info(f"Task : {task}")

    if request.method == "POST":
        response = requests.put(
            f"http://{backend_host}/update/task/{id}",
            json = {"description" : form.description.data}
        )
        return redirect(url_for('home'))

    return render_template('update_task.html', task=task, form=form)

# update location

# dele

@app.route('/delete/task/<int:id>')
def delete_task(id):
    response = requests.delete(f"http://{backend_host}/delete/task/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

