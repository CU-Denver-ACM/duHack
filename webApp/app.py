from flask import Flask, render_template, request
import CourseParser

app = Flask(__name__)

@app.route("/", methods=["POST", "GET", "PUT"])
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


if __name__ == "__main__":
    app.run(debug=True)