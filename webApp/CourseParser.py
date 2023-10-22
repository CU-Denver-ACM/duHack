import Course
import json

def parse_csci_courselist():
    """
    Parse the csci courselist json and return a list of math course objects
    """
    with open("course_info/course_list_CSCI.json") as csci_course_file:
        csci_data = json.load(csci_course_file)
    csci_data_keys = csci_data.keys()
 
    csci_course_list = []
    for course in csci_data_keys:
        new_course = Course.Course(csci_data[course]["course_name"], course, csci_data[course]["course_description"], csci_data[course]["offered"], csci_data[course]["prereqs"], csci_data[course]["credits"])
        csci_course_list.append(new_course)
    
    return csci_course_list



def parse_math_courselist():
    """
    Parse the math courselist json and return a list of math course objects
    """
    with open("course_info/course_list_MATH.json") as math_course_file:
        math_data = json.load(math_course_file)
    math_data_keys = math_data.keys()
 
    math_course_list = []
    for course in math_data_keys:
        new_course = Course.Course(math_data[course]["course_name"], course, math_data[course]["course_description"],math_data[course]["offered"], math_data[course]["prereqs"], math_data[course]["credits"])
        math_course_list.append(new_course)
    
    return math_course_list


def parse_engl_courselist():
    """
    Parse the math courselist json and return a list of math course objects
    """
    with open("course_info/course_list_ENGL.json") as engl_course_file:
        engl_data = json.load(engl_course_file)
    engl_data_keys = engl_data.keys()
 
    engl_course_list = []
    for course in engl_data_keys:
        new_course = Course.Course(engl_data[course]["course_name"], course, engl_data[course]["course_description"], engl_data[course]["offered"], engl_data[course]["prereqs"], engl_data[course]["credits"])
        engl_course_list.append(new_course)
    
    return engl_course_list


