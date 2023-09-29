#meant to implement firbase
#default_app = firebase_admin.initialize_app()

# imports
import os                 # os is used to get environment variables IP & PORT
import json
import requests

from flask import Flask, jsonify  # Flask is the web app that we will customize

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/api', methods=['GET', 'POST'])
def get_nutrition():
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    payload = json.dumps({
        "query": "chicken noodle soup"
    })
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': '3a83fb27',
        'x-app-key': '135db1d7aaba12d363ad7b2225656590'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    return jsonify(response)

if __name__ == 'main':
   app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)