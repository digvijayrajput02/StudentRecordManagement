"""Marks entry and result calculation."""


def add_or_update_marks(manager, student_id, marks):
    if manager.update_marks(student_id, marks):
        print("Marks saved successfully.")
    else:
        print("Student not found.")


def calculate_result(student):
    marks = student.get("marks", {})
    if not marks:
        return {"total": 0, "percentage": 0.0, "grade": "Not available"}

    total = sum(marks.values())
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return {"total": total, "percentage": percentage, "grade": grade}
