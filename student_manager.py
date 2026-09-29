"""Functions for adding, searching, updating and deleting student records."""
from file_handler import load_students, save_students
from student import create_student


class StudentManager:
    def __init__(self):
        self.students = load_students()

    def _save(self):
        save_students(self.students)

    def add_student(self, student_id, name, course, semester):
        if self.find_student(student_id):
            raise ValueError("A student with this ID already exists.")
        self.students.append(create_student(student_id, name, course, semester))
        self._save()
        print("Student added successfully.")

    def get_all_students(self):
        return sorted(self.students, key=lambda student: student["student_id"])

    def find_student(self, student_id):
        for student in self.students:
            if student["student_id"].lower() == student_id.lower():
                return student
        return None

    def update_student(self, student_id, name, course, semester):
        student = self.find_student(student_id)
        if not student:
            return False
        student["name"] = name
        student["course"] = course
        student["semester"] = semester
        self._save()
        print("Student details updated successfully.")
        return True

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if not student:
            return False
        self.students.remove(student)
        self._save()
        return True

    def update_marks(self, student_id, marks):
        student = self.find_student(student_id)
        if not student:
            return False
        student["marks"].update(marks)
        self._save()
        return True
