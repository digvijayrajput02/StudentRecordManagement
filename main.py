"""Entry point for the Student Record Management System."""
from student_manager import StudentManager
from marks_manager import add_or_update_marks
from report_manager import show_all_students, show_student_report
from validators import read_non_empty, read_student_id, read_mark


def print_menu():
    print("\n" + "=" * 42)
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 42)
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student details")
    print("5. Delete student")
    print("6. Add / update marks")
    print("7. View student result")
    print("8. Exit")


def main():
    manager = StudentManager()
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()

        try:
            if choice == "1":
                student_id = read_student_id("Enter student ID: ")
                name = read_non_empty("Enter student name: ")
                course = read_non_empty("Enter course name: ")
                semester = read_non_empty("Enter semester: ")
                manager.add_student(student_id, name, course, semester)

            elif choice == "2":
                show_all_students(manager.get_all_students())

            elif choice == "3":
                student_id = read_student_id("Enter student ID to search: ")
                student = manager.find_student(student_id)
                if student:
                    show_student_report(student)
                else:
                    print("Student not found.")

            elif choice == "4":
                student_id = read_student_id("Enter student ID to update: ")
                student = manager.find_student(student_id)
                if not student:
                    print("Student not found.")
                    continue
                print("Press Enter to keep the current value.")
                name = input(f"Name [{student['name']}]: ").strip() or student["name"]
                course = input(f"Course [{student['course']}]: ").strip() or student["course"]
                semester = input(f"Semester [{student['semester']}]: ").strip() or student["semester"]
                manager.update_student(student_id, name, course, semester)

            elif choice == "5":
                student_id = read_student_id("Enter student ID to delete: ")
                if manager.delete_student(student_id):
                    print("Student deleted successfully.")
                else:
                    print("Student not found.")

            elif choice == "6":
                student_id = read_student_id("Enter student ID: ")
                student = manager.find_student(student_id)
                if not student:
                    print("Student not found. Add the student first.")
                    continue
                subject_count = int(input("How many subjects? "))
                if subject_count <= 0 or subject_count > 20:
                    print("Enter a subject count from 1 to 20.")
                    continue
                marks = {}
                for number in range(1, subject_count + 1):
                    subject = read_non_empty(f"Subject {number} name: ")
                    marks[subject] = read_mark(f"Marks for {subject} (0-100): ")
                add_or_update_marks(manager, student_id, marks)

            elif choice == "7":
                student_id = read_student_id("Enter student ID: ")
                student = manager.find_student(student_id)
                if student:
                    show_student_report(student)
                else:
                    print("Student not found.")

            elif choice == "8":
                print("Data is saved automatically. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 8.")

        except ValueError as error:
            print(f"Input error: {error}")
        except (OSError, json.JSONDecodeError) as error:
            print(f"Storage error: {error}")
        except Exception as error:
            # Final safety net; unexpected errors are shown without crashing the menu.
            print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
