########################################################################
# Project: Spraoi                                                      #
# Description: Research on impact of gamification in user engagement   #
# Author: Participants on ADAPT CENTRE Hackathon #1 (Dublin, 02/10/15) # 
# License: Open Source (GPL)                                           #
######################################################################## 


# Imports
import config # Configuration constants
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB initialization
client = MongoClient( config.MONGODB_PROD_URI )
db = client.get_default_database()


@app.route('/')

def spraoi():

  _items = db.users.find()
  items = [item for item in _items]

  return render_template('spraoi.html', items=items)


@app.route('/new', methods=['POST'])
def new():

  item_doc = {
    'email': request.form['email'],
    'password': request.form['password']
  }
  db.users.insert_one(item_doc)

  return redirect(url_for('spraoi'))


# Run service
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=False)
