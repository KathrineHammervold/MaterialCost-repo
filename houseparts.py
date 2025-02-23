
from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #Enable CORS for all routes

@app.route("/get_house_parts", methods=["GET"])
def index():
    #return "Hello world"
    return house_parts()

# Read Excel file and convert to JSON
def get_house_parts():
    df = pd.read_excel("houseparts.xlsx")
    return df.to_dict(orient="records")

#@app.route("/get_house_parts", methods=["GET"])
def house_parts():
    return jsonify(get_house_parts())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
