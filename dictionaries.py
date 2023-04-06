#student = ["Kevin", "Sheldon", "Brian", "John", "Joy"]
estates = ["Kasarani", "Exit 9", "Syokimau", "Kayole", "Ngara"]

students = {
    "Kevin":"Kasarani",
    "Sheldon":"Exit 9",
    "Brian":"Syokimau",
    "John":"Kayole",
    "Joy":"Ngara"   
}

"""print(students["Kevin"])"""

for student in students:
    print(student, students[student], sep=" - ")