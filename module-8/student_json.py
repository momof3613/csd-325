# Name: Ajanae Stanback
# Assignment: Module 8.2 - JSON Practice
# Date: November 26, 2026
# Description: Read, display, and update student records
# using a JSON file.

import json

# Load the original student list.
with open("Student.json", "r") as file:
    student_list = json.load(file)


def display_students(students):
    """Display each student's name, ID, and email."""
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")


# Display the original student list.
print("This is the original Student list:")
display_students(student_list)

# Add a new student to the list.
new_student = {
    "F_Name": "Ajanae",
    "L_Name": "Stanback",
    "Student_ID": 78901,
    "Email": "astanback@example.com"
}

student_list.append(new_student)

# Display the updated student list.
print("\nThis is the updated Student list:")
display_students(student_list)

# Save the updated student list to the JSON file.
with open("Student.json", "w") as file:
    json.dump(student_list, file, indent=4)

# Notify the user that the file was updated.
print("\nThe Student.json file was updated successfully.")

