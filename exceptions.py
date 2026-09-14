class InvalidMarksError(Exception):
    """Exception raised for errors in the marks.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Marks must be numeric and between 0 and 100"):
        self.message = message
        super().__init__(self.message)

class InvalidStudentDataError(Exception):
    """Exception raised for errors in the student information.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Missing or invalid student information"):
        self.message = message
        super().__init__(self.message)
