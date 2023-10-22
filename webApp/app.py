from flask import Flask, render_template, request, jsonify, session, url_for, redirect
import CourseParser
from Student import Student

app = Flask(__name__)

listOfStudents = [
    Student("Kyle Ren", 1234, "BS", "Math", "kyler", "helloworld"),
    Student("Jim Broman", 5467, "BA", "Math", "liftingLyfe", "gainzzzzz"),
    Student("Adrien Agreste", 7865, "BS", "marketing", "agreste1", "cataclysm")
]

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/add-courses", methods=["POST", "GET", "PUT"])
def add_courses():
    if request.method == "POST":
        i = 1;
        course_selection = []
        course_iteration = request.form.getlist(f"items{i}")
        while course_iteration != []:
            course_selection.append(course_iteration[0])
            i+=1
            course_iteration = request.form.getlist(f"items{i}")
        print(course_selection)
        return render_template("add_courses.html", options=CourseParser.combined())
    if request.method == "GET":
        return render_template("add_courses.html", options=CourseParser.combined())

@app.route("/login", methods=['GET'])
def get_login():
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def login():
    # Get request data
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    is_found = False
    # Placeholder authentication logic
    for student in listOfStudents:
        if student.get_username() == username and student.get_password() == password:
            is_found = True
            break

    if is_found:
        session['username'] = username
        return render_template("add_courses.html")

    else:
        return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("home.html")


@app.route("/signup", methods=['GET'])
def get_signup():
    return render_template("signup.html")

@app.route("/signup", methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    sid = data.get('id')
    major = data.get('major')
    minor = data.get('minor')

    # typically store the user data in a database
    listOfStudents.append(Student(name, sid, major, minor, username, password))
    return render_template("login.html")

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


if __name__ == "__main__":
    app.run(debug=True)
