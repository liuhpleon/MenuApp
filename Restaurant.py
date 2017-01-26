from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
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
@app.route('/restaurant/<int:restaurant_id>/addItem/',methods=['GET','POST'])
def addItem(restaurant_id):
    if request.method == 'POST':
        newItem = Menu(name = request.form['name'],
                       description = request.form['description'],
                       course = request.form['course'],
                       price = request.form['price'],
                       restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()
        flash("item created")
        return redirect(url_for('restaurant_Menu',restaurant_id=restaurant_id))
    else:
        return render_template('add.html',restaurant_id=restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/',methods=['GET','POST'])
def edit(restaurant_id,menu_id):
    item = session.query(Menu).filter_by(id=menu_id).one()
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        item.price = request.form['price']
        item.course = request.form['course']
        session.add(item)
        session.commit()
        flash("item edited")
        return redirect(url_for('restaurant_Menu',restaurant_id=restaurant_id))
    else:
        return render_template('edit.html',restaurant_id = restaurant_id,menu_id=item.id,item = item)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/',methods=['GET','POST'])
def delete(restaurant_id,menu_id):
    name = session.query(Menu).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(name)
        flash("item deleted")
        return redirect(url_for('restaurant_Menu',restaurant_id=restaurant_id))
    else:
        return render_template('delete.html',restaurant_id=restaurant_id,menu_id=name.id,name = name)

@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def transferToJSON(restaurant_id):
    items = session.query(Menu).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(Menus = [i.transfer for i in items])
    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run('0.0.0.0',port = 5000)
    
    