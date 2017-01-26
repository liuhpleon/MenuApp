from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB_setup import base, Restaurant, Menu
engine = create_engine('sqlite:///restaurant_menu.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()
app = Flask(__name__)
@app.route('/')
@app.route('/restaurants/')
def restaurants():
    restaurants = session.query(Restaurant).all();
    return render_template('restaurant.html',restaurants = restaurants)

@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_Menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(Menu).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html',restaurant = restaurant,items = items)
    '''
    output = ""
    output+=restaurant.name+"<br>"
    output+="<br>"
    for item in items:
        output+=item.name+"<br>"
        output+=item.price+"<br>"
        output+=item.description+"<br>"
    return output
    '''
@app.route('/restaurant/<int:restaurant_id>/addItem/')
def addItem(restaurant_id):
    return "addItem working";

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def edit(restaurant_id,menu_id):
    return "wait edit"

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def delete(restaurant_id,menu_id):
    name = session.query(Menu).filter_by(id=menu_id).one()
    session.delete(name)
    return 'wait delete'


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',port = 5000)
    