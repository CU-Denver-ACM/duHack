class Student:
  __name = ""
  __ID = ""
  __major = ""
  __minor = ""
  __username = ""
  __password = ""
  __coursesTaken = []
  def __init__(self, name:str, ID:int,  major, minor:str, un:str, pw:str) -> None:
      self.__name = name
      self.__ID = ID
      self.__major = major
      self.__minor = minor if minor is not None else None
      self.__username = un if un is not None else (self.__name[0:3]+str(self.__ID)[-3:-1])
      self.__password = pw if pw is not None else "Pass123!"


  def __str__(self) -> str:
      if(self.__minor == None):
          return (f"Student Name: {self.__name}, Student ID: {self.__ID}, Major: {self.__major}, "
                  f"Username: {self.__username}")
      else:   
          return (f"Student Name: {self.__name}, Student ID: {self.__ID}, Major: {self.__major}, Minor: {self.__minor}, "
                  f"Username: {self.__username}")

  def set_student(self, name, ID,  major, minor, un, pw):
      if name == None:
          pass
      else:
          self.__name = name
      if ID == None:
          pass
      else:
          self.__ID = ID
      if major == None:
          pass
      else:
          self.__major = major
      if minor == None:
          pass
      else:
          self.__minor = minor
      if un == None:
          pass
      else:
          self.__username = un
      if pw == None:   
          pass
      else:
          self.__password = pw

  def get_name(self):
    return self.__name

  def get_ID(self):
    return self.__ID

  def get_major(self):
    return self.__major

  def get_minor(self):
    return self.__minor

  def get_username(self):
    return self.__username

  def get_password(self):
    return self.__password
