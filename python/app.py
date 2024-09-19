import flask
from flask import Flask, jsonify
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data')
def get_data():
    # Fetch data from a public API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    
    # Convert to DataFrame and perform a simple operation
    df = pd.DataFrame(data)
    summary = df['userId'].value_counts().to_dict()
    
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)
