import json
import pickle
from flask import Flask, request
import numpy as np
from src.cleaning_text import Text
from typing import Dict, Any
from database.postgres import Database


classifier_path = ('/app/model/pipe.pkl')

with open(classifier_path, 'rb') as classifier:
    model = pickle.load(classifier)


app = Flask(__name__)
database = Database()

def __process_input(request_data: str) -> np.array:
    parsed_body = np.asarray(json.loads(request_data)["descriptions"])
    assert len(parsed_body) != 0
    prepared_text = Text(parsed_body).clean_text()
    return np.asarray(prepared_text)


@app.route("/predict", methods=["POST"])
def predict() -> Dict[str, Any]:
    try:
        input_params = __process_input(request.data)
        predictions = model.predict(input_params)

        input = json.loads(request.data)
        output = {"Wine ratings": predictions.tolist()}
        
        database.insert(json.dumps(input), json.dumps(output))

        return json.dumps(output)

    except (KeyError, json.JSONDecodeError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except AssertionError:
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500


@app.route("/inferences", methods=["GET"])
def inferences() -> Dict[str, Any]:
    try:
        database = Database()
        inferences = database.get_last_ten_inferences()
        return json.dumps(inferences)
    except Exception:
        return json.dumps({"error": "COULD NOT GET INFERENCES"}), 500


if __name__ == "__main__":
    app.run()
