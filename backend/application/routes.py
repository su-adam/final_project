from application import app, db
from application.models import Galleries, Locations
from flask import render_template, request, redirect, url_for, jsonify, Response

# Location add, read - start with 
# CRUD for galleries

 
@app.route('/create/location', methods=['POST'])
def create_location():
        package = request.json
        new_location = Locations(description=package["description"])
        db.session.add(new_task)
        db.session.commit()
        return Response(f"Your location: {new_task.description} has been added", mimetype='text/plain')



@app.route('/read/allLocations', methods=['GET'])
def read_tasks():
    all_locations = Locations.query.all()
    locations_dict = {"locations": []}
    for location in all_locations:
        locations_dict["locations"].append(
            {
                "id" : location.id,
                "description": task.description,
            }
        )
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

