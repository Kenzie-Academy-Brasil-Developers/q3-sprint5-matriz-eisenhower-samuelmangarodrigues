from enum import unique
from unicodedata import category
from sqlalchemy import Column,String,Integer,Text,ForeignKey
from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy.orm import relationship
from app.models.tasks_categories_table import task_categories

@dataclass
class TasksModel(db.Model):
    id:int
    name:str
    description:str
    duration:int

    __tablename__="tasks"
    
    id = Column(Integer, primary_key = True)
    name = Column(String(100), unique=True, nullable = False)
    description = Column(Text) 
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhowers_id = Column(
        Integer,
        ForeignKey('eisenhowers.id'),
        nullable = False
        )
    categories = relationship("CategoriesModel", secondary = task_categories, backref="tasks")
    

