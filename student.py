"""Student record data structure."""


def create_student(student_id, name, course, semester):
    """Return a student record as a dictionary."""
    return {
        "student_id": student_id,
        "name": name,
        "course": course,
        "semester": semester,
        "marks": {}
    }
