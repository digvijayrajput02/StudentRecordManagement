# Student Record Management System

A beginner-friendly Python Essentials project that manages student details and subject-wise marks. It includes a Streamlit web interface and a command-line interface, with local JSON storage.

## Features
- Register and view student records
- Delete a selected student record with a confirmation checkbox
- Add or update subject-wise marks
- Calculate total marks, average percentage, and grade
- Persist records in `data/students.json`
- Input checks and duplicate-ID protection
- Modular Python files and automated unit tests

## Technologies
- Python 3.10+
- Streamlit (web interface)
- JSON file storage
- `unittest` for basic automated tests

## Run the Streamlit app
1. Install Python 3.10 or newer.
2. Open a terminal in the `StudentRecordManagement` folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Start the web app:
   ```bash
   python -m streamlit run app.py
   ```
5. Open the local URL printed in the terminal (usually `http://localhost:8501`).

## Run the command-line version
```bash
python main.py
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Project structure
- `app.py` — Streamlit user interface
- `main.py` — command-line menu
- `student.py` — student record creation
- `student_manager.py` — add, search, update, delete and marks operations
- `marks_manager.py` — total, average percentage and grade calculation
- `report_manager.py` — console reports
- `file_handler.py` — JSON loading and saving
- `validators.py` — reusable input validation helpers
- `data/students.json` — local student records
- `tests/test_project.py` — unit tests for result calculation
- `docs/diagrams/` — project design diagrams
- `Project_Report.pdf` — detailed project report for review

## Calculation note
Marks are expected on a 0–100 scale. The displayed percentage is the arithmetic mean of the entered subject marks. Grade boundaries are illustrative project rules in `marks_manager.py`, not an official university grading scheme.

## Limitations
This is a local educational demonstration, not a secure production system. It does not implement authentication, cloud storage, or role-based access. Avoid storing sensitive real student data.
