
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("")
def index():
    return "Hello world"



# Read Excel file and convert to JSON
def get_house_parts():
    df = pd.read_excel("houseparts.xlsx")
    return df.to_dict(orient="records")

@app.route("/get_house_parts", methods=["GET"])
def house_parts():
    return jsonify(get_house_parts())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
app.run(host="0.0.0.0", port=80)
