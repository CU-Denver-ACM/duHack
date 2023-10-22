class Course:
    def __init__(self, name, course_id, description, offered, prereqs=None, credits=None):
        """
        Initializes a Course object.

        :param name: Name of the course (str)
        :param course_id: ID code of the course (str)
        :param prereqs: List of prerequisite courses (list of Course objects). Default is an empty list.
        :param category: Category of the course (str). Possible values: "core", "elective", "breadth" etc.
        """
        self.name = name
        self.course_id = course_id
        self.description = description
        self.prereqs = prereqs if prereqs is not None else []
        self.credits = credits
        self.offered = offered

    def __str__(self):
        return f"{self.course_id}: {self.name}"

    def add_prerequisite(self, course):
        """
        Add a prerequisite course to the list.

        :param course: Course object to be added as a prerequisite.
        """
        if course not in self.prereqs:
            self.prereqs.append(course)

    def get_offered(self):
        """Get offered terms"""
        return self.offered
    

# Example usage
# math101 = Course(name="Math 101", course_id="MTH101", category="core")
# comp101 = Course(name="Computer Science 101", course_id="CSC101", category="core")
# comp201 = Course(name="Computer Science 201", course_id="CSC201", prereqs=[math101, comp101], category="core")

# print(comp201)
