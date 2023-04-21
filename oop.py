class Student:
    """
    The function defines a class called Student with attributes for name, estates, and course, and a
    string representation method.
    :return: The code is defining a class called "Student" with an initializer method that takes in
    three parameters: "name", "estates", and "course". If the "name" parameter is not provided, a
    ValueError is raised. The class also has a "__str__" method that returns a string representation of
    the object, including the name, estates, and course of the student. However, there
    """
    def __init__(self, name, estates, course):
        if not name:
            raise ValueError("Please provide your name")
        self.name = name
        self.estates = estates
        self.course = course

def __str__(self):
    return f"{self.name} is from {self.estates} and is doing {self.course}"

#Getter for the estate
@property
def estates(self):
    return self._estates

#Setter for the estate
@estates.setter
def estates(self, estates):
    if estates not in ["Tena", "South B", "Umoja 1", "Umoja 2", "Karen"]:
        raise ValueError("Inavalid Estate")
    self._estates = estates

def main():
    student = get_student()
    print(f"{student.name} is from {student.estates} and is doing {student.course}")


def get_student():
    """
    The function prompts the user to input their name, estate, and course, creates a Student object with
    the input values, and returns the object.
    :return: The function `get_student()` returns an instance of the `Student` class with attributes
    `name`, `estates`, and `course` that are obtained from user input.
    """
    name = input("What's your name? ").strip()
    estates = input("Which estate do you come from? ").strip()
    course = input("Which course do you do? ").strip()
    student = Student(name, estates, course)
    return student


if __name__ == "__main__":
    main()