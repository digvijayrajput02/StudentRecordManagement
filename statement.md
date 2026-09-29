# Project Statement

## Project title
Student Record Management System

## Problem statement
Maintaining student details and marks manually can create repeated work, inconsistent records, and delays when finding a student's information. This project provides a small Python application to organize student details and subject-wise marks in a local JSON file.

## Objectives
1. Register and display student details.
2. Remove a selected student record.
3. Store or update subject-wise marks.
4. Calculate total marks, average percentage, and a simple grade.
5. Practise functions, loops, conditions, lists, dictionaries, modules, file handling, validation, and error handling.

## Intended users
A student or teacher using a local computer for a small academic demonstration.

## Scope
The application offers a Streamlit web interface and a command-line interface. Student data is stored locally in `data/students.json`. The current Streamlit interface supports adding, viewing and deleting students, plus marks entry and result display. The underlying manager also contains student search and update operations, available through the Python module and command-line workflow where exposed.

## High-level features
- Student registration and listing
- Student deletion with a confirmation step in the web interface
- Subject-wise marks entry and updates
- Total, average percentage and grade calculation
- Local JSON persistence
- Modular source files and basic unit tests

## Non-functional requirements
- **Usability:** clear labels, prompts, and navigation.
- **Reliability:** successful changes are written to local JSON storage.
- **Maintainability:** responsibilities are separated into modules.
- **Input validation:** empty fields and duplicate student IDs are checked; marks are constrained to 0–100 in the web interface.
- **Resource efficiency:** local file storage and standard Python data structures suit a small demonstration dataset.

## Limitations
This is a beginner-level educational project. It does not include login, permissions, cloud backup, or production-grade security. Grade boundaries are illustrative and should be adjusted if an official grading policy is required.
