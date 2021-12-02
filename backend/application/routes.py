from application import app, db
from application.models import Galleries, Locations
from flask import render_template, request, redirect, url_for, jsonify, Response

 
@app.route('/create/location', methods=['POST'])
def create_location():
        package = request.json
        new_location = Locations(
            country_name = package["country_name"],
            city = package["city"]
        )
        db.session.add(new_location)
        db.session.commit()
        return Response(f"Your location: {new_location.country_name} has been added", mimetype='text/plain')




@app.route('/read/allLocations', methods=['GET'])
def read_allLocations():
    all_locations = Locations.query.all()
    locations_dict = {"locations": []}
    for location in all_locations:
        galleries=[]
        for gallery in location.galleries:
            galleries.append(
                {
                    "id" : gallery.id,
                    "gallery_name": gallery.gallery_name,
                    "information" : gallery.information,
                    "fee" : gallery.fee,
                    "country_id" : location.country_name
                }
            )
        locations_dict["locations"].append(
            {
                "id" : location.id,
                "country": location.country_name,
                "city" : location.city,
                "galleries" : galleries
            }
        )
    
    return jsonify(locations_dict)


@app.route('/create/gallery', methods=['POST'])
def create_gallery():
        package = request.json
        new_gallery = Galleries(
            gallery_name = package["gallery_name"],
            information = package["information"],
            fee = package["fee"],
            country_id = package["country_id"]
            )
        db.session.add(new_gallery)
        db.session.commit()
        return Response(f"Your galley: {new_gallery.gallery_name} has been added", mimetype='text/plain')



@app.route('/read/allGalleries', methods=['GET'])
def read_allgalleries():
    all_galleries = Galleries.query.all()
    galleries_dict = {"galleries": []}
    for gallery in all_galleries:
        galleries_dict["galleries"].append(
            {
                "id" : gallery.id,
                "gallery_name" : gallery.gallery_name,
                "information" : gallery.information,
                "fee" : gallery.fee
                
            }
        )
    return jsonify(galleries_dict)



@app.route('/update/gallery/<int:id>', methods=['PUT'])
def update_galleries(id):
    package = request.json
    gallery = Galleries.query.get(id)
    gallery.gallery_name = package["gallery_name"]
    gallery.information = package["information"]
    gallery.fee = package["fee"]
    db.session.commit()
    return Response(f" Updated task (ID : {id}) with {gallery.gallery_name} now updated", mimetype='text/plain')

    

@app.route('/delete/gallery/<int:id>', methods=['DELETE'])
def delete_gallery(id):
    gallery = Galleries.query.get(id)
    db.session.delete(gallery)
    db.session.commit()
    return Response(f" Deleted gallery with ID : {id}", mimetype='text/plain')

