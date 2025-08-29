# CourseFlow CLI

A simple Python-based command-line application that manages **students, courses, and enrollments**.  
It demonstrates core concepts of:

- Command-line interaction  
- Data persistence with JSON  
- CRUD operations for multiple entities  

---

## Features

This application enables the user:

- To **create, view, update, and delete students**  
- To **create, view, update, and delete courses**  
- To **enroll students in courses** and manage their enrollments  
- To **view enrolled students in a course**  
- To **search for students, courses, or enrollments by ID**  
- To **automatically persist data** in a `db.json` file  

---

## File Structure

courseflow-cli/
├── lib/
│ ├── cli.py # CLI workflow & menus
│ ├── db/
│ │ ├── student.py # Student model & CRUD
│ │ ├── course.py # Course model & CRUD
│ │ └── enrollment.py # Enrollment model & CRUD
├── main.py # Entry point for the program
├── db.json # Persistent storage
└── README.md # Project documentation

---

## How It Works

When the user runs the program, they see a **main menu**:

--- CourseFlow CLI ---

1. Manage Students

2. Manage Courses

3. Manage Enrollments

4. Exit

From there, users can navigate sub-menus:

- **Student Menu**
  - Create student
  - View all students
  - Find student by ID
  - Update student
  - Delete student  

- **Course Menu**
  - Create course
  - View all courses
  - Find course by ID
  - Update course
  - Delete course
  - View enrolled students  

- **Enrollment Menu**
  - Create enrollment
  - View all enrollments
  - Find enrollment by ID
  - Delete enrollment  

All data is saved into `db.json` and reloaded on startup.  

---

## ▶️ How To Run

Clone the repository:

```bash
1. git clone https://github.com/your-username/courseflow-cli.git
cd courseflow-cli
2. Run the program:

2. python -m lib.cli

 Validation Rules
- Students must have a unique ID, valid name, and email

- Courses must have a title and credit value

- Enrollments must link a valid student and course

- Duplicate enrollments (same student + same course) are not allowed

 Future Improvements
- Prevent duplicate student emails and duplicate course titles

- Add confirmation prompts before deleting data

- Export reports (CSV / JSON)

- Switch storage from JSON → SQLite for scalability

- Add unit tests

- Build a GUI or web-based frontend

License
- This project is licensed under the MIT License.
