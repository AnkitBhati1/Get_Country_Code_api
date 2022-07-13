from flask import Flask, jsonify, request
from markupsafe import escape
import pyarrow.parquet as pq
import pandas as pd
import numpy as np

df = pd.read_parquet('continent_data_new.parquet')

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.post("/")
def country_data():
    
    if request.method == "POST":
        country_name = request.get_json().get('country_name', None)
        if country_name is None:
            return jsonify({"error": "No country name provided"})
        else:
            country_name = country_name.lower()
            # country_name = country_name.capitalize()
            country_name = country_name.replace(' ', '_')
            country_name = country_name.replace('-', "")
            country_name = country_name.replace('.', "")
            country_name = country_name.replace('/', "")
            country_name = country_name.replace('\\', "")
            country_name = country_name.replace('(', "")
            country_name = country_name.replace(')', "")
            country_name = country_name.replace('[', "")
            country_name = country_name.replace(']', "")
            country_name = country_name.replace('{', "")
            country_name = country_name.replace('}', "")
            country_name = country_name.replace('+', "")
            country_name = country_name.replace('*', "")
            country_name = country_name.replace('&', "")
            country_name = country_name.replace('%', "")
            country_name = country_name.replace('$', "")
            country_name = country_name.replace('#', "")
            country_name = country_name.replace('@', "")
            country_name = country_name.replace('!', "")
            country_name = country_name.replace('~', "")
            country_name = country_name.replace('`', "")
            country_name = country_name.replace('^', "")
            country_name = country_name.replace('&', "")
            country_name = country_name.replace('%', "")
            country_name = country_name.replace('$', "")
            country_name = country_name.replace('#', "")
            country_name = country_name.replace('@', "")
            country_name = country_name.replace('!', "")
            country_data = df[df['Country_new'] == country_name]
            if country_data.empty:
                return jsonify({"error": "Country not found"})
            else:
                # remove country_new column
                country_data = country_data.drop(columns=['Country_new'])
        
                return jsonify(country_data.to_dict(orient='records'))


@app.post('/login')
def login_post():
    return "hello"
        