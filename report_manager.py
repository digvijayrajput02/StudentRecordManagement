"""Console reports for student records."""
from marks_manager import calculate_result


def show_all_students(students):
    if not students:
        print("No student records found.")
        return

    print("\nSTUDENT LIST")
    print("-" * 72)
    print(f"{'ID':<15}{'Name':<24}{'Course':<23}{'Semester':<10}")
    print("-" * 72)
    for student in students:
        print(
            f"{student['student_id']:<15}"
            f"{student['name'][:22]:<24}"
            f"{student['course'][:21]:<23}"
            f"{student['semester']:<10}"
        )


def show_student_report(student):
    result = calculate_result(student)
    print("\nSTUDENT DETAILS")
    print("-" * 35)
    print(f"Student ID : {student['student_id']}")
    print(f"Name       : {student['name']}")
    print(f"Course     : {student['course']}")
    print(f"Semester   : {student['semester']}")
    print("\nMARKS")
    if student.get("marks"):
        for subject, mark in student["marks"].items():
            print(f"{subject}: {mark}/100")
    else:
        print("No marks entered yet.")
    print("\nRESULT SUMMARY")
    print(f"Total marks : {result['total']}")
    print(f"Percentage  : {result['percentage']:.2f}%")
    print(f"Grade       : {result['grade']}")
