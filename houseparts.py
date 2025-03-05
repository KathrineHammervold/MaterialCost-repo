
from flask import Flask, jsonify, request
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
    return get_house_parts()

@app.route("/get_supplier_and_cost", methods=["GET"])
def get_supplier_and_cost_route():
    material = request.args.get('material')
    return get_supplier_and_cost(material)

"""
@app.route("/get_units_and_quantity", methods=["GET"])
def get_units_and_quantity_route():
    return get_units_and_quantity()

"""
# Read the sheet in the Excel file that contains parts and materials and convert to JSON
def get_house_parts():
    try:
        df = pd.read_excel("houseparts.xlsx")
        df = pd.read_excel("houseparts.xlsx", engine="openpyxl", sheet_name="House parts and materials")
    except FileNotFoundError:
        logging.error("The file houseparts.xlsx was not found.")
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred"}), 500
    return jsonify(df.to_dict(orient="records"))


def get_supplier_and_cost(material):
    logging.info(f"Material: {material}")
    try:
        df = pd.read_excel("houseparts.xlsx", engine="openpyxl", sheet_name="Supplier and cost")
        dict = df.to_dict(orient="records")
        logging.info(f"Dict: {dict}")
        material = material.strip("'").lower()
        for item in dict:
            logging.info(f"Item: {item}")
            logging.info(f"Item Material: {item['Material']}")
            logging.info(f"Variable material #{material}#")
            logging.info(f"Suppliers: {item['Supplier']}")
            logging.info(f"Cost per unit: {item['Cost per unit']}")
        filtered_data = [item for item in dict if item["Material"].strip().lower() == material]
        #filtered_data = df[df["Material"].str.lower() == material.lower()]
        logging.info(f"Filtered data: {filtered_data}")
        #logging.info(f"Filtered data: {filtered_data.to_dict(orient='records')}")
    except FileNotFoundError:
        logging.error("The file houseparts.xlsx was not found.")
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred"}), 500
    return jsonify(filtered_data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
