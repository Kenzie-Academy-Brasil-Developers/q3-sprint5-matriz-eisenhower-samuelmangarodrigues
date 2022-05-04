from flask import Blueprint
from app.controllers.tasks_controller import create_tasks,att_tasks,delete_tasks


bp_tasks=Blueprint("tasks",__name__,url_prefix="/tasks")
bp_tasks.post("")(create_tasks)
bp_tasks.patch("/<int:id>")(att_tasks)
bp_tasks.delete("/<int:id>")(delete_tasks)



