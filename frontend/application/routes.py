from application import app
from application.forms import CreatelocationForm, CreategalleryForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "final_project_backend:5000"


@app.route('/')
@app.route('/home')
def home():
    locations = requests.get(f"http://{backend_host}/read/allLocations").json()["locations"]
    app.logger.info(f"Locations: {locations}")
    return render_template('index.html', title="Home", locations=locations)


@app.route('/create/location', methods=['GET','POST'])
def create_location():
    form = CreatelocationForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/location",
            json = {
                "country" : form.country.data,
                "city" : form.city.data
                
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_location.html", title="Select location", form=form)



@app.route('/create/gallery', methods=['GET','POST'])
def create_gallery():
    form = CreategalleryForm()

    json = requests.get(f"http://{backend_host}/read/allLocations").json()
    for location in json["locations"]:
        form.country.choices.append((location["id"], location["country"]))

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/gallery",
            json = {
                "name" : form.name.data,
                "information" : form.information.data,
                "fee" : form.fee.data
                
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_gallery.html", title="Select location", form=form)

@app.route('/update/gallery/<int:id>', methods=['GET','POST'])
def update_gallery(id):
    form = CreategalleryForm()
    gallery = requests.get(f"http://{backend_host}/read/gallery{id}").json()
    app.logger.info(f"Gallery : {gallery}")

    if request.method == "POST":
        response = requests.put(
            f"http://{backend_host}/update/gallery/{id}",
            json = {
                    "name" : form.name.data,
                    "information" : form.information.data,
                    "fee" : form.fee.data
                    
                }
        )
        return redirect(url_for('home'))

    return render_template('update.html', task=task, form=form)



@app.route('/delete/gallery/<int:id>')
def delete_gallery(id):
    response = requests.delete(f"http://{backend_host}/delete/gallery/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

