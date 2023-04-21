# The class "Firstname" initializes an object with a name attribute and raises a value error if no
# name is specified.
class Firstname:
    def __init__(self, name):
        if not name:
            raise ValueError("No name specified")
        self.name = name

# The class "Student" takes in a name and course as parameters and initializes them as attributes.
class Student(Firstname):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def __str__(self):
        """
        The function returns a string that includes the name and course of a student.
        :return: The `__str__` method is returning a string that includes the name of the student and the
        course they are studying. The format of the string is using f-strings, which allows for the values
        of `self.name` and `self.course` to be inserted into the string.
        """
        return f"{self.name} is studying {self.course}"

# The class "Teacher" takes in a name and units and returns a string indicating the teacher's name and
# the units they are teaching.
class Teacher(Firstname):
    def __init__(self, name, units):
        super().__init__(name)
        self.units =units

    def __str__(self):
        return f"{self.name} is is teaching {self.units}"

def main():
    """
    The function creates instances of the Student and Teacher classes and prints them.
    """
    student = Student("Bostone", "Information Science")
    teacher = Teacher("Ochieng", "Python Programming")
    print(student)
    print(teacher)

if __name__ == "__main__":
    main()
