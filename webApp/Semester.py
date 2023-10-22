class Semester:
  def __init__(self, name: str = "", course_list: list = [], credits: int = 0):
      self.__name = name
      self.__course_list = course_list
      self.__credits = credits

  # Getter methods for private variables
  def get_name(self):
      return self.__name

  def get_course_list(self):
      return self.__course_list

  def get_credits(self):
      return self.__credits

  # Setter methods for private variables
  def set_name(self, name: str):
      self.__name = name

  def set_course_list(self, course_list: list):
      self.__course_list = course_list

  def set_credits(self, credits: int):
      self.__credits = credits

  
