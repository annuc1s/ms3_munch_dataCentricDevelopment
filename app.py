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

#Creates a route to sign-in.html
@app.route('/log_in')
def log_in():
    return render_template("sign-in.html")

# Routing through existing users and decrypting their password from database
@app.route('/sign_in', methods= ['POST'])
def sign_in():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    #Compares the detailes entered with details in database from registering
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), 
            login_user['password']
            ) == login_user['password']:
            session['username'] = request.form['username']
            #If the details entered match it will redirect the user book_table
            return redirect(url_for('book_table'))

    return 'Invalid username/password combination'

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

#allows for looping through db collection party_size
@app.route('/book_table')
def book_table():
    return render_template("book-tbl.html",
    people=mongo.db.party_size.find()
    )

#Allows reservation form to be submitted
#and stores data in MongoDB within a reservations collection
#after successful submission, the user is redirected to edit_reservation
@app.route('/reserve_table', methods=['POST'])
def reserve_table():

    reservations = mongo.db.reservations
    username = session['username']
    make_reservation = {
        "username": username,
        "reservation_name": request.form.get("reservation_name"),
        "contact_number": request.form.get("contact_number"),
        "reservation_date": request.form.get("reservation_date"),
        "reservation_time": request.form.get("reservation_time"),
        "party_size": request.form.get("party_size"),
        "additional_info": request.form.get("additional_info")
    }
    reservations.insert_one(make_reservation)
    #reservations.insert_one(request.form.to_dict())
    return redirect(url_for('review_reservation'))
  
@app.route('/review_reservation')
def review_reservation():
    return render_template('review-reservation.html')

"""@app.route('/review_reservation/<reservations_id>', methods=['GET'])
def review_reservation(reservations_id):
    reserved = mongo.db.reservations.find_one({'_id': ObjectId(reservations._id)})
    return render_template('review-reservation.html', reservations=reserved)"""


#Allows the user to delete their reservation from the database
#Returns them to the url_for('book_table)
@app.route('/delete_reservation/<reservations_id>')
def delete_reservation(reservations_id):
    mongo.db.reservations.remove({'id': ObjectId(reservations_id)})

    return redirect(url_for('book_table'))

@app.route('/edit_reservation')
def edit_reservation():
    return render_template('edit-reservation.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)