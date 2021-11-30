from application import app, db
from application.models import Galleries, Location
from flask import render_template, request, redirect, url_for, jsonify, Response


 
@app.route('/create/location', methods=['POST'])
def create_locaton():
        package = request.json
        new_location = Location(description=package["description"])
        db.session.add(new_location)
        db.session.commit()
        return Response(f"New area: {new_location.area}", mimetype='text/plain')



# @app.route('/read/locations', methods=['GET'])
# def read_tasks():
#     all_tasks = Tasks.query.all()
#     tasks_dict = {"tasks": []}
#     for task in all_tasks:
#         tasks_dict["tasks"].append(
#             {
#                 "id" : task.id,
#                 "description": task.description,
#                 "completed": task.completed
#             }
#         )
#     return jsonify(tasks_dict)

# @app.route('/read/location/<int:id>', methods=['GET'])
# def read_task(id):
#     tasks = Tasks.query.get(id)
#     tasks_dict = {
#                 "id" : task.id,
#                 "description": task.description,
#                 "completed": task.completed
#             }
#     return jsonify(tasks_dict)

# @app.route('/update/location/<int:id>', methods=['PUT'])
# def update_task(id):
#     package = request.json
#     task = Tasks.query.get(id)
#     task.description = package["description"]
#     db.session.commit()
#     return Response(f" Updated task (ID : {id}) with {task.description}", mimetype='text/plain')

    

# @app.route('/delete/location/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     task = Tasks.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return Response(f" Deleted task with ID : {id}", mimetype='text/plain')

