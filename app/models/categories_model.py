from sqlalchemy import Column,String,Integer,Text
from dataclasses import dataclass
from app.configs.database import db

@dataclass
class CategoriesModel(db.Model):
    
    id:int
    name:str
    description:str
    
    __tablename__="categories"

    id = Column(Integer,primary_key = True)
    name = Column(String(100), unique = True, nullable = False)
    description = Column(Text)