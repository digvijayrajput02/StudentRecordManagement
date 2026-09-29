"""Reusable input validation helpers."""


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_student_id(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Student ID cannot be empty.")


def read_mark(prompt):
    while True:
        try:
            mark = float(input(prompt).strip())
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
