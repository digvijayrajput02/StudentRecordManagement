import streamlit as st
from student_manager import StudentManager
from marks_manager import calculate_result

st.set_page_config(page_title="Student Record Management", page_icon="🎓", layout="wide")

@st.cache_resource
def get_manager():
    return StudentManager()

manager = get_manager()

st.title("🎓 Student Record Management System")
st.caption("A Python Essentials project for managing student details and academic marks.")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a section", ["Dashboard", "Add Student", "View Students", "Marks & Results"])

if page == "Dashboard":
    students = manager.get_all_students()
    st.header("Dashboard")
    percentages = [calculate_result(s)["percentage"] for s in students if s.get("marks")]
    average = sum(percentages) / len(percentages) if percentages else 0
    total_subject_entries = sum(len(s.get("marks", {})) for s in students)
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Students", len(students))
    c2.metric("Subject Entries", total_subject_entries)
    c3.metric("Average Percentage", f"{average:.2f}%")
    st.subheader("Student Records")
    if students:
        st.dataframe([{"Student ID": s["student_id"], "Name": s["name"], "Course": s["course"], "Semester": s["semester"]} for s in students], use_container_width=True, hide_index=True)
    else:
        st.info("No students yet. Use Add Student to register the first record.")

elif page == "Add Student":
    st.header("Register a Student")
    with st.form("add_student_form"):
        student_id = st.text_input("Student ID").strip()
        name = st.text_input("Full Name").strip()
        course = st.text_input("Course").strip()
        semester = st.number_input("Semester", min_value=1, max_value=12, step=1)
        submitted = st.form_submit_button("Save Student")
    if submitted:
        if not student_id or not name or not course:
            st.error("Please fill in all fields.")
        else:
            try:
                manager.add_student(student_id, name, course, str(semester))
                st.success("Student saved successfully.")
                st.rerun()
            except ValueError as error:
                st.error(str(error))

elif page == "View Students":
    st.header("Student Records")
    students = manager.get_all_students()
    if students:
        st.dataframe([{"Student ID": s["student_id"], "Name": s["name"], "Course": s["course"], "Semester": s["semester"]} for s in students], use_container_width=True, hide_index=True)
        st.subheader("Delete a Student")
        ids = [s["student_id"] for s in students]
        with st.form("delete_student_form"):
            selected_id = st.selectbox("Select Student ID", ids)
            confirm = st.checkbox("I confirm that I want to delete this record.")
            delete_clicked = st.form_submit_button("Delete Student")
        if delete_clicked:
            if not confirm:
                st.warning("Please confirm before deleting.")
            elif manager.delete_student(selected_id):
                st.success("Student record deleted.")
                st.rerun()
            else:
                st.error("Student not found.")
    else:
        st.info("No student records found. Add a student first.")

elif page == "Marks & Results":
    st.header("Marks & Results")
    students = manager.get_all_students()
    if not students:
        st.warning("Please add a student before entering marks.")
    else:
        options = {f'{s["student_id"]} — {s["name"]}': s["student_id"] for s in students}
        selected_label = st.selectbox("Select Student", list(options.keys()))
        selected_id = options[selected_label]
        with st.form("marks_form"):
            subject = st.text_input("Subject Name").strip()
            mark = st.number_input("Marks (0–100)", min_value=0.0, max_value=100.0, step=1.0)
            save_marks = st.form_submit_button("Save Marks")
        if save_marks:
            if not subject:
                st.error("Please enter a subject name.")
            else:
                if manager.update_marks(selected_id, {subject: mark}):
                    st.success(f"Marks saved for {subject}.")
                    st.rerun()
                else:
                    st.error("Student not found.")
        student = manager.find_student(selected_id)
        marks = student.get("marks", {}) if student else {}
        st.subheader("Student Result")
        if marks:
            st.dataframe([{"Subject": name, "Marks": score, "Out Of": 100} for name, score in marks.items()], use_container_width=True, hide_index=True)
            result = calculate_result(student)
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Marks", result["total"])
            c2.metric("Average Percentage", f'{result["percentage"]:.2f}%')
            c3.metric("Grade", result["grade"])
        else:
            st.info("No marks entered for this student yet.")
