from sqlalchemy import Column,String,Integer
from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy.orm import relationship

@dataclass
class EisenhowersModel(db.Model):
    id:int
    type:str

    __tablename__="eisenhowers"

    id = Column(Integer, primary_key=True)
    type = Column(String(100))
    
    tasks = relationship("TasksModel",backref="eisenhowers")