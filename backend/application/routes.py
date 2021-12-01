from application import app, db
from application.models import Galleries, Locations
from flask import render_template, request, redirect, url_for, jsonify, Response

 
@app.route('/create/location', methods=['POST'])
def create_location():
        package = request.json
        new_location = Locations(description=package["description"])
        db.session.add(new_location)
        db.session.commit()
        return Response(f"Your location: {new_location.description} has been added", mimetype='text/plain')



@app.route('/read/allLocations', methods=['GET'])
def read_tasks():
    all_locations = Locations.query.all()
    locations_dict = {"locations": []}
    for location in all_locations:
        locations_dict["locations"].append(
            {
                "id" : location.id,
                "description": location.description,
            }
        )
    return jsonify(locations_dict)

@app.route('/create/gallery', methods=['POST'])
def create_gallery():
        package = request.json
        new_gallery = Galleries(gallery_name=package["gallery_name"])
        db.session.add(new_gallery)
        db.session.commit()
        return Response(f"Your galley: {new_gallery.description} has been added", mimetype='text/plain')



@app.route('/read/allGalleries', methods=['GET'])
def read_allgalleries():
    all_galleries = Galleries.query.all()
    galleries_dict = {"galleries": []}
    for gallery in all_galleries:
        galleries_dict["galleries"].append(
            {
                "id" : galleries.id,
                "gallery_name" : galleries.description,
                "information" : galleries.informaiton,
                "fee" : galleries.fee
            }
        )
    return jsonify(galleries_dict)



@app.route('/update/gallery/<int:id>', methods=['PUT'])
def update_galleries(id):
    package = request.json
    gallery = Galleries.query.get(id)
    gallery.gallery_name = package["description"]
    db.session.commit()
    return Response(f" Updated task (ID : {id}) with {gallery.gallery_name}", mimetype='text/plain')

    

@app.route('/delete/gallery/<int:id>', methods=['DELETE'])
def delete_gallery(id):
    gallery = Galleries.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return Response(f" Deleted task with ID : {id}", mimetype='text/plain')

