from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB_setup import base, Restaurant, Menu
engine = create_engine('sqlite:///restaurant_menu.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()
'''
items = session.query(Menu).all()
for item in items:
    print item.name+" "+item.description+" "+item.price+" "+item.course+" "+item.restaurant.name
vbs = session.query(Menu).filter_by(name = 'Veggie Burger')
for vb in vbs:
    print vb.id
    print vb.price
    print vb.restaurant.name
urban_vb = session.query(Menu).filter_by(id = 8).one()
print urban_vb.price
urban_vb.price = "$1.09"
session.add(urban_vb)
session.commit()
vbs = session.query(Menu).filter_by(name = 'Veggie Burger')
for vb in vbs:
    if vb.price!='$1.09':
        vb.price = '$1.09'
        session.add(vb);
        session.commit()
for vb in vbs:
    print vb.id
    print vb.price
    print vb.restaurant.name
'''
spinach = session.query(Menu).filter_by(name='Spinach Ice Cream').one()
print spinach.restaurant.id
rest = session.query(Restaurant).filter_by(id = 7).one()
session.delete(spinach)
session.commit
r = session.query(Menu).filter_by(restaurant = rest).all()
for item in r:
    print item.name


                                        