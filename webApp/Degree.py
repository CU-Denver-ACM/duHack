class Degree:
  def __init__(self, track="", course_list=None, categories=None):
      self.track = track
      self.course_list = course_list if course_list is not None else []
      self.categories = categories if categories is not None else []
      self.category_count = {}
      
   

  def add_course(self, course):
      self.course_list.append(course)

  def add_category(self, category):
      self.categories.append(category)

  def increment_category_count(self, category , value):
      self.categoryCount[category] = value
