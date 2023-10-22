from typing import final
from Student import Student
from Semester import Semester
from Degree import Degree
from Course import Course
from CourseParser import parse_csci_courselist
from CourseParser import parse_math_courselist
from CourseParser import parse_engl_courselist

BS_DEGREE_GENED_COUNT = 6
BS_DEGREE_BREADTH_COUNT = 5
BS_DEGREE_TECH_ELECTIVE_COUNT = 4
BS_DEGREE_SCIENCE_COUNT = 2

BA_DEGREE_GENED_COUNT = 6
BA_DEGREE_SCIENCE_COUNT = 2
BA_FREE_ELECTIVE_COUNT = 12
BA_TECH_ELECTIVE_COUNT = 7


BS_CATEGORIES = ["BS_MAIN_TRACK", "BS_GENEDS", "BS_SCIENCE", "BS_BREADTH", "BS_TECH_ELECTIVES"]

BS_DEGREE_MAIN_TRACK = ["CSCI1410", "CSCI1411", "MATH1401", "ENGR1200","ENGL1020", "CSCI2312","CSCI2511", "CSCI1510", "ENGL2030" , "CSCI2421", "CSCI2525", "MATH2411", "CSCI3287", "CSCI3412", "CSCI3761", "MATH3195", "CSCI3415", "CSCI3453","CSCI3508", "CSCI4551", "CSCI4738", "CSCI4034", "CSCI4591", "CSCI4739"]

BS_COUNTS = {"BS_GENEDS" : 6 ,"BS_BREADTH" : 5, "BS_TECH_ELECTIVES" : 5 , "BS_SCIENCE" : 2 }



BA_CATEGORIES = ["BA_MAIN_TRACK" , "BA_GENEDS" , "BA_SCIENCE" , "BA_FREE_ELECTIVES" , "BA_TECH_ELECTIVES"]

BA_DEGREE_MAIN_TRACK = ["CSCI1410", "CSCI1411", "ENGR1200", "ENGL1020", "CSCI2312","MATH1401", "ENGL2030" ,"CSCI2421", "CSCI2511", "CSCI3412", "CSCI3508", "CSCI3287"]

BA_COUNTS = {"BA_GENEDS" : 6 , "BA_SCIENCE" : 2 , "BA_FREE_ELECTIVES" : 12 , "BA_TECH_ELECTIVES" : 7}



degree = BS_DEGREE_MAIN_TRACK

def prereqs(courseToAdd, allPrereqsNeeded, coursesTaken):
  
  for item in courseToAdd.prereqs:
      if (courseToAdd not in coursesTaken and course not in allPrereqsNeeded):
          allPrereqsNeeded.append(courseToAdd)  # Append the prerequisite, not the courseToAdd
         # print(allPrereqsNeeded)
          allPrereqsNeeded = prereqs(course, allPrereqsNeeded, coursesTaken)  # Recurse on the prerequisite

  return allPrereqsNeeded

coursesToTake = []

student = Student("James Reynolds" , 123456789 , "BS","" ,   "james.a.reynolds@ucdenver.edu" , "testPassword")

if (student.get_major == "BS"):
  
  degree = BS_DEGREE_MAIN_TRACK
else:
  degree = BA_DEGREE_MAIN_TRACK
coursesToTake = []

degreeCourseObjects = []
fullCSCICourseList = parse_csci_courselist()

for course in degree:
  for object in fullCSCICourseList:
   
    if (course == object.course_id):
      degreeCourseObjects.append(object)
  

student.__coursesTaken = ["CSCI1510", "CSCI3412"]
for course in degreeCourseObjects:
  
  if (course.course_id in  student.__coursesTaken):
    continue
  else:
      
    coursesToTake.append(course)


#print(coursesToTake)
schedule = [] 
for i in range(20):
  schedule.append(Semester())
  print(schedule[i])

print (len(schedule))

#fullMathCourseList = parse_math_courselist()
#fullEnglishCourseList = parse_engl_courselist()





prereqsNeeded = []
currentSemester = 0
if student.get_major == "BS":
  finalCategories = BS_CATEGORIES

  
else:
  finalCategories = BA_CATEGORIES


#print(prereqsNeeded)
#for course in degree:
  #check for prereqs
for course in coursesToTake:
  #print(course)
  prereqsNeeded.append( prereqs(course, [], student.__coursesTaken))
  finalPrereqs = []
  finalprereqObjects = []
  for i in prereqsNeeded:
    for j in i:
      finalPrereqs.append(j.course_id)
      finalprereqObjects.append(j)
  if len(prereqsNeeded) == 0:
    schedule[currentSemester].add_course(course)
    print("test")
    while schedule[currentSemester].get_credits() >= 15:
      currentSemester +=1
    print(schedule[currentSemester].get_credits())
    schedule[currentSemester].add_credits(3)
   # print(schedule)
  else:
    finalprereqObjects = []
    finalPrereqs = []
    if (len(finalPrereqs) != 0):
      for i in prereqsNeeded:
        for j in i:
          finalPrereqs.append(j.course_id)
          finalprereqObjects.append(j)
    precedences = {}
    
    prereqsToCourses = []
   
    initialprecedence = 0
    
    for prereq1 in finalprereqObjects:
      for prereq2 in prereq1.prereqs:
       # print(prereq2)
        if prereq2 in finalPrereqs:
          if precedences.get(prereq1) is not None:
          
            precedences[prereq2] = (precedences[prereq1] + 1)
            
         # precedences[prereq2] = precedences.get(prereq1) + 1
    #precedences[finalPrereqs[0]] = 0
    print(schedule[currentSemester].get_credits())
    while schedule[currentSemester].get_credits() >= 15:
      currentSemester +=1

    for prereq in finalprereqObjects:
      if prereq in precedences:
        schedule[(currentSemester + precedences[prereq])].add_course(prereq)
        schedule[currentSemester].add_credits(3)
        

for semester in schedule:
  print(semester.get_course_list())