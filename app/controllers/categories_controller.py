from flask import jsonify, request
from app.models.categories_model import CategoriesModel
from sqlalchemy.orm.session import Session
from app.configs.database import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

def create_category():
    try:
        data = request.get_json()
        session : Session = db.session
        cat = CategoriesModel(**data)

        session.add(cat)
        session.commit()


        return jsonify(cat),201                                    
    except IntegrityError:
            return {"msg": "category already exists!"},409
  


def att_category(id):
    try:
        data = request.get_json()
        cat = CategoriesModel.query.get(id)    
        session : Session = db.session    
        for key, value in data.items():
                setattr(cat, key, value)

        session.add(cat)
        session.commit()
        return jsonify(cat),200
    except AttributeError:
            return {"msg": "category not found!"},404

def delete_category(id):
    try:    
        query = CategoriesModel.query.get(id)
        session : Session = db.session    

        session.delete(query)
        session.commit()
        return '',204
    except UnmappedInstanceError:
        return {"msg": "category not found!"},404

def get_all():
    categories_all=(CategoriesModel.query.all())
    
    lista = []
    for cata in categories_all:
        obj={"id":cata.id,
            "name":cata.name,
            "description":cata.description,
            "tasks":cata.tasks}
        lista.append(obj)
     


    return {"categories":[lis for lis in lista]}