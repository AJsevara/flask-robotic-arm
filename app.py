from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

servo_positions = {
    "base": 90,
    "shoulder": 90,
    "elbow": 90,
    "wrist": 90,
    "gripper-rotation": 90,
    "gripper": 90
}

@app.route("/update_servo", methods=["POST"])
def update_servo():
    data = request.json
    for key, value in data.items():
        if key in servo_positions:
            servo_positions[key] = int(value)  # Update servo position

    return jsonify({"message": "Servo updated", "positions": servo_positions})

@app.route("/get_servo_positions", methods=["GET"])
def get_servo_positions():
    return jsonify(servo_positions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
