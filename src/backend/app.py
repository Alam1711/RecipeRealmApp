#implement firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
default_app = firebase_admin.initialize_app()

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize

app = Flask(__name__)     # create an app

# decorator to associate
# a function with the url
@app.route("/")
def showHomePage():
      # response from the server
    return "This is home page"
 
if __name__ == "__main__":
  app.run(host="0.0.0.0")
