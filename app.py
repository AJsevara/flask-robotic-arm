from flask import Flask, request, jsonify

app = Flask(__name__)

servo_positions = {
    "base": 90,
    "shoulder": 90,
    "elbow": 90,
    "wrist": 90,
    "gripper": 90
}

@app.route('/update_servo', methods=['GET'])
def update_servo():
    servo = request.args.get('servo')
    value = request.args.get('value')
    if servo and value:
        servo_positions[servo] = int(value)
        return jsonify({"status": "success", "servo": servo, "value": value})
    return jsonify({"status": "error", "message": "Invalid parameters"})

@app.route('/get_servo_positions', methods=['GET'])
def get_servo_positions():
    return jsonify(servo_positions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
