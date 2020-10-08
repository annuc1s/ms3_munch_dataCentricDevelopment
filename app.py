import os
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId 

app = Flask(__name__)
#database name and uri linking to that database
app.config["MONGO_DBNAME"] = 'munch_menu'
app.config["MONGO_URI"] = 'mongodb+srv://RGz8TLF1RmPmQvu9:MunCH_ms3@cluster0.gsp9j.mongodb.net/munch_menu?retryWrites=true&w=majority'


#variables used throughout the app
mongo = PyMongo(app)



@app.route('/')
@app.route('/get_menu')
def get_menu():
#call items from MONGO collection menu_items
    return render_template("index.html", 
        snacks=mongo.db.appetizers_snacks.find(), 
        burgers=mongo.db.gourmet_burgers.find(),
        toppings=mongo.db.toppings_sides.find(),
        milkshakes=mongo.db.milkshakes.find(),
    )

@app.route('/sign_in', methods= ['POST', 'GET'])
def sign_in():
    return render_template ("sign-in.html")


# Routing through registering a new user and encrypting their password for security
@app.route('/sign_up', methods= ['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            # if there isn't an existing user with the chosen username
            # a new user is added to the database
            # and the password is encrypted (hashed)
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass })
            session['username'] = request.form['username']
            # After creating new user date they are redirected to 'book_tbl'
            return redirect (url_for('book_table'))

        return  'This username already exists!'
    return render_template('sign-in.html')


@app.route('/book_table')
def book_table():
    return render_template("book-tbl.html")

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)