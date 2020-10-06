import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId 

app = Flask(__name__)
#database name and uri linking to that database
app.config["MONGO_DBNAME"] = 'munch_menu'
app.config["MONGO_URI"] = 'mongodb+srv://RGz8TLF1RmPmQvu9:MunCH_ms3@cluster0.gsp9j.mongodb.net/munch_menu?retryWrites=true&w=majority'

#app added using the constructor method
mongo = PyMongo(app)

@app.route('/')
@app.route('/get_snacks')

def get_snacks():
#call items from MONGO collection menu_items
    return render_template("index.html", 
        snacks=mongo.db.appetizers_snacks.find(), 
        burgers=mongo.db.gourmet_burgers.find(),
        toppings=mongo.db.toppings_sides.find(),
        milkshakes=mongo.db.milkshakes.find(),
    )


@app.route('/get_burgers')

def get_burgers():
    return render_template("index.html", burgers=mongo.db.menu_items.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)