import mysql.connector


class Course:
    def __init__(self, subject: str, number: int, title: str = ""):
        self.__subject = subject
        self.__number = number
        self.__title = title

    def __str__(self):
        return f"""{self.subject}:{self.__number:04}"""
        pass

    @property
    def subject(self):
        return self.__subject

    @property
    def number(self):
        return self.__number

    @property
    def title(self):
        return self.__title

    # #################### LOADING DATA FROM DATABASE ####################
    # -----------------------------------------------------------------------------------------------------------------
    def load(self, db_config : dict):
        """
        Loads the data for the current object. Assume subject and number is loaded in the object.
        :param db_config: a dictionary as described in Readme.md with the connection information.
        """
        # TODO: implement Course.load
        pass

    # -----------------------------------------------------------------------------------------------------------------
    def load_all(db_config : dict) -> []:
        """
        Class method.
        Loads all the courses and returns the list
        :param db_config: a dictionary as described in Readme.md with the connection information.
        :return the list of all loaded courses from the db.
        """
        # TODO: implement Course.load_all
        pass

    # -----------------------------------------------------------------------------------------------------------------
    def load_all_subject(db_config : dict, subject: str) -> []:
        """
        Class method.
        Loads all the courses with "subject" in the course's subject.
        The search should be done in the DB and is case insensitive.
            Hint: remember that `like "%abc%"` will return all rows where abc is anywhere in the column.
        :param db_config: a dictionary as described in Readme.md with the connection information.
        :param subject: subject to search for.
        :return: the list of all loaded courses from the db.
        """
        # TODO: implement Course.load_all_subject
        pass

    pass
