
from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
CORS(app) #Enable CORS for all routes

@app.after_request
def after_request(response):
    logging.info("Request processed")
    return response

@app.route("/get_house_parts", methods=["GET"])
def get_house_parts_route():
    return house_parts()

# Read Excel file and convert to JSON
def get_house_parts():
    try:
        df = pd.read_excel("houseparts.xlsx")
    except FileNotFoundError:
        logging.error("The file houseparts.xlsx was not found.")
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred"}), 500
    return df.to_dict(orient="records")

#@app.route("/get_house_parts", methods=["GET"])
def house_parts():
    return jsonify(get_house_parts())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
