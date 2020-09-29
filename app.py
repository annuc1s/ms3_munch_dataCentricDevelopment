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
@app.route('/get_items')

def get_items():
#call items from MONGO collection menu_items
    return render_template("index.html", items=mongo.db.menu_items.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)