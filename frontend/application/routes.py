from application import app
from application.forms import LocationForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "final_project-backend:5000"

# read locations, create gallery, read gallery, update gallery, delete gallery

@app.route('/')
@app.route('/home')
def home():
    all_locations = requests.get(f"http://{backend_host}/read/allLocations").json()
    all_galleries = request.get(f"http://{backend_host}/read/allGalleries").json()
    app.logger.info(f"Locations: {all_locations}")
    return render_template('index.html', title="Home", all_locations=all_locations["locations"])


@app.route('/create/location', methods=['GET','POST'])
def create_location():
    form = LocationForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/location",
            json = {"location" : form.location.data}
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_location.html", title="Select location", form=form)

#change to galleries

@app.route('/update/gallery/<int:id>', methods=['GET','POST'])
def update_gallery(id):
    form = GalleryForm()
    gallery = requests.get(f"http://{backend_host}/read/task{id}").json()
    app.logger.info(f"Location : {location}")

    if request.method == "POST":
        response = requests.put(
            f"http://{backend_host}/update/task/{id}",
            json = {"location" : form.description.data}
        )
        return redirect(url_for('home'))

    return render_template('update_location.html', task=task, form=form)



@app.route('/delete/location/<int:id>')
def delete_task(id):
    response = requests.delete(f"http://{backend_host}/delete/task/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

