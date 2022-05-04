from flask import Blueprint
from app.controllers.categories_controller import att_category,create_category,delete_category, get_all


bp_categories = Blueprint("categories",__name__,url_prefix='/categories')
bp_categories.post("")(create_category)
bp_categories.patch("/<int:id>")(att_category)
bp_categories.delete("/<int:id>")(delete_category)
bp_categories.get("")(get_all)