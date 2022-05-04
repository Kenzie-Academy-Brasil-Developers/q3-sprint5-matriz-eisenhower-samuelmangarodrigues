from app.routes import categories_blueprint,tasks_blueprint
from flask import Flask

def init_app(app:Flask):
    app.register_blueprint(categories_blueprint.bp_categories)
    app.register_blueprint(tasks_blueprint.bp_tasks)
