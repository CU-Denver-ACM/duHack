from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello there<p>"

@app.route("/login", methods=['POST'])
def login():
    # Get request data
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Placeholder authentication logic
    if username == "test" and password == "password":
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials."}), 401

@app.route("/signup", methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Placeholder signup logic
    # You would typically store the user data in a database
    return jsonify({"message": "Signup successful!"}), 200

@app.route("/get-schedule", methods=['GET'])
def get_schedule():
    # Placeholder logic to fetch the user's schedule
    # Typically, you'd fetch from a database based on the user's ID
    schedule = {
        "Monday": "9AM - 5PM",
        "Tuesday": "10AM - 4PM",
        # ... add other days here
    }
    return jsonify(schedule)

@app.route("/enter-schedule", methods=['POST'])
def enter_schedule():
    data = request.get_json()

    # Placeholder logic to enter the user's schedule
    # Typically, you'd store this in a database under the user's ID
    schedule = data.get('schedule')

    return jsonify({"message": "Schedule entered successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
