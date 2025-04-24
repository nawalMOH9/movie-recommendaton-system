from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
import methods as m



app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Welcome to Movie Recommendation System</h1>"


@app.route('/recommend', methods=['POST'])
def predict():
    q = request.get_json()
  
    result = m.get_similar_items(q)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)