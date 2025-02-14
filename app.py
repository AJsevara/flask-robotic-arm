from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend access

# Dictionary to store servo positions
servo_positions = {
    "base": 90,
    "shoulder": 90,
    "elbow": 90,
    "wrist": 90,
    "gripper_rotation": 90,
    "gripper": 90
}

@app.route('/')
def home():
    return "Flask app is running successfully! 🚀"

# Route to update servo position
@app.route('/update_servo', methods=['POST'])
def update_servo():
    data = request.get_json()
    servo = data.get("servo")
    value = data.get("value")
    
    if servo in servo_positions:
        servo_positions[servo] = value
        return jsonify({"message": f"{servo} updated to {value}°"}), 200
    else:
        return jsonify({"error": "Invalid servo name"}), 400

# Route to get current servo positions
@app.route('/get_servo_positions', methods=['GET'])
def get_servo_positions():
    return jsonify(servo_positions)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
