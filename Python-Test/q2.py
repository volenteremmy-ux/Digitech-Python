student = {
    "name": "Ali",
    "age": 17,
    "grade": "B"
}

student["grade"] = "A"

student_name = student.get("name")
print("Student Name:", student_name)

all_keys = student.keys()
print("All Keys:", all_keys)