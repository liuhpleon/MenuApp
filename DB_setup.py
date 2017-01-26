from sqlalchemy import Column, ForeignKey, Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

base = declarative_base()

class Restaurant(base):
    __tablename__ = 'restaurant'
    name = Column(String(80),nullable = False)
    id = Column(Integer,primary_key = True)

class Menu(base):
    __tablename__ = 'menu'
    name = Column(String(80),nullable = False)
    id = Column(Integer,primary_key = True)
    course = Column(String(80))
    description = Column(String(300))
    price= Column(String(10))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    @property
    def transfer(self):
        return{
               'name':self.name,
               'course':self.course,
               'price':self.price,
               'description':self.description,
               'id':self.id,
        }
    
engine = create_engine('sqlite:///restaurant_menu.db')
base.metadata.create_all(engine)