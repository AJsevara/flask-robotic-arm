from flask import Flask, request, jsonify

app = Flask(__name__)

# Store servo positions in memory (or use a database)
servo_positions = {
    "base": 90,
    "shoulder": 90,
    "elbow": 90,
    "wrist": 90,
    "gripper-rotation": 90,
    "gripper": 90
}

@app.route("/")
def home():
    return "Robotic Arm Backend is Running!"

@app.route("/update_servo", methods=["POST"])
def update_servo():
    data = request.json
    servo = data.get("servo")
    value = data.get("value")

    if servo in servo_positions:
        servo_positions[servo] = int(value)
        return jsonify({"status": "success", "servo": servo, "value": value})

    return jsonify({"status": "error", "message": "Invalid servo"}), 400

@app.route("/get_servo_positions", methods=["GET"])
def get_servo_positions():
    return jsonify(servo_positions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
