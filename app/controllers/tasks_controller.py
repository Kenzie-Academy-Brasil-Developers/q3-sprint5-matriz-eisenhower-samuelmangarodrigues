from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from app.models.tasks_model import TasksModel
from sqlalchemy.orm import Session
from app.configs.database import db
from app.models.categories_model import CategoriesModel
from sqlalchemy.exc import DataError


def create_tasks():
    try:
        session : Session = db.session
        data = request.get_json()
        categories = data.pop('categories')

        
        if data['importance'] > 2 or data['importance'] < 1:
            return {  "msg": {
                "valid_options": {
                "importance": [1, 2],
                "urgency": [1, 2]
                },
                "recieved_options": {
                "importance": data['importance'],
                "urgency": data['urgency']
                }
            }},404

        if data['urgency'] > 2 or data['urgency'] < 1:
            return {  "msg": {
                "valid_options": {
                "importance": [1, 2],
                "urgency": [1, 2]
                },
                "recieved_options": {
                "importance": data['importance'],
                "urgency": data['urgency']
                }
            }},404
            
        if data['urgency'] == 1 and data['importance'] == 1:
            data['eisenhowers_id'] = 1
        if data['urgency']==1 and data['importance']==2:
            data['eisenhowers_id'] = 2
        if data['urgency']==2 and data['importance']==1:
            data['eisenhowers_id'] = 3
        if data['urgency']==2 and data['importance']==2:
            data['eisenhowers_id'] = 4

        if "name" not in data:
            return {"msg":"Campos faltando"},400
        

        
        new_task = TasksModel(**data)


        for cat in categories:
            equal_cats = CategoriesModel.query.filter_by(name = cat).first()
            if equal_cats:
                new_task.categories.append(equal_cats)
                session.add(new_task)
                session.commit()
            else:
                new_cat = CategoriesModel(name = cat)
                session.add(new_cat)
                session.commit()
                new_task.categories.append(new_cat)

        return {
        "id": new_task.id,
        "name":new_task.name,
        "description": new_task.description,
        "duration": new_task.duration,
        "classification": new_task.eisenhowers.type,
        "categories": new_task.categories
        },201

    except IntegrityError:
        return { "msg":"task already exist"},404

    except DataError:
        return {"msg":"Only integer values"},400

 

def att_tasks(id):


    try:
        session: Session = db.session
        data = request.get_json()
        task= TasksModel.query.get(id)


        if "urgency" not in data:
            data['urgency']=task.urgency
        
        if "importance" not in data:
            data['importance']=task.importance

        if data['urgency']==1 and data['importance']==1:
                data['eisenhowers_id'] = 1
        if data['urgency']==1 and data['importance']==2:
                data['eisenhowers_id'] = 2
        if data['urgency']==2 and data['importance']==1:
                data['eisenhowers_id'] = 3
        if data['urgency']==2 and data['importance']==2:
                data['eisenhowers_id'] = 4


        session.add(task)
        session.commit()

        for key, value in data.items():
            setattr(task, key, value)

        

        return {
                "id": task.id,
                "name":task.name,
                "description": task.description,
                "duration": task.duration,
                "classification": task.eisenhowers.type,
                "categories": [cat.name for cat in task.categories]
            }
    except KeyError:
        return ""

def delete_tasks(id):
      
        task = TasksModel.query.get(id)
        session : Session = db.session    

        if not task:
            return {'msg': f'Task {id} not found!'}, 404

        session.delete(task)
        session.commit()

        return '',204
