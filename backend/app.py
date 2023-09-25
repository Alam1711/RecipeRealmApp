#meant to implement firbase
#default_app = firebase_admin.initialize_app()

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize

app = Flask(__name__)     # create an app
