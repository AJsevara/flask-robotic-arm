from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)

# Allow all origins and methods (GET, POST, etc.)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

servo_positions = {
    "base": 90,
    "elbow": 90,
    "gripper": 90,
    "gripper-rotation": 90,
    "shoulder": 90,
    "wrist": 90
}

@app.route('/get_servo_positions', methods=['GET'])
def get_servo_positions():
    return jsonify(servo_positions)  # Return JSON response

@app.route('/update_servo', methods=['OPTIONS'])
def preflight():
    """Handles preflight requests for CORS"""
    response = jsonify({'message': 'CORS preflight successful'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

@app.route('/update_servo', methods=['POST'])
def update_servo():
    data = request.json
    for key in data:
        if key in servo_positions:
            servo_positions[key] = data[key]

    response = jsonify({"message": "Servo updated", "data": servo_positions})
    response.headers.add('Access-Control-Allow-Origin', '*')  # Explicitly allow frontend
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
