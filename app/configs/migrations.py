from flask import Flask 
from flask_migrate import Migrate

def init_app(app:Flask):

    from app.models.categories_model import CategoriesModel
    from app.models.eisenhowers_model import EisenhowersModel
    from app.models.tasks_categories_table import task_categories
    from app.models.tasks_model import TasksModel
    
    Migrate(app,app.db)