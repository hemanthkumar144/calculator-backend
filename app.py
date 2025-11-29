from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    expression = data.get("expression")

    try:
        # Evaluate the math expression safely
        result = eval(expression)
        return jsonify({"result": result})
    except:
        return jsonify({"error": "Invalid Expression"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
