"""Read and write student records using a JSON file."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "students.json"


def load_students():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("The data file must contain a list of student records.")
        return data
    except json.JSONDecodeError as error:
        raise ValueError("students.json is not valid JSON. Restore or correct the file.") from error


def save_students(students):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_file = DATA_FILE.with_suffix(".tmp")
    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)
    temporary_file.replace(DATA_FILE)
