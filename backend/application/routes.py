from application import app, db
from application.models import Galleries, Locations
from flask import render_template, request, redirect, url_for, jsonify, Response

# CRUD for galleries
# Location add, read - start with 
 
@app.route('/create/location', methods=['POST'])
def create_locaton():
        package = request.json
        new_location = Locations(location=package["location"])
        db.session.add(new_location)
        db.session.commit()
        return Response(f"New area: {new_location.area}", mimetype='text/plain')



@app.route('/read/locations', methods=['GET'])
def read_locations():
    all_locations = Locations.query.all()
    locations_dict = {"locations": []}
    for location in all_locationss:
        locations_dict["locations"].append(
            {
                "id" : location.id,
                "description": location.location
            }
        )
    return jsonify(tasks_dict)


@app.route('/read/location/<int:id>', methods=['GET'])
def read_location(id):
    locations = Locations.query.get(id)
    locations_dict = {
                "id" : location.id,
                "description": location.location
            }
    return jsonify(locations_dict)

# @app.route('/update/location/<int:id>', methods=['PUT'])
# def update_task(id):
#     package = request.json
#     location = Locations.query.get(id)
#     task.description = package["description"]
#     db.session.commit()
#     return Response(f" Updated task (ID : {id}) with {task.description}", mimetype='text/plain')

    

# @app.route('/delete/location/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     task = Tasks.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return Response(f" Deleted task with ID : {id}", mimetype='text/plain')

