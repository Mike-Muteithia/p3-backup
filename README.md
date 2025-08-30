# CourseFlow CLI

- CourseFlow is a command-line application for managing students, courses, and enrollments using **Python**, **SQLAlchemy ORM**, and **Alembic** for migrations.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd courseflow

2. Install dependencies with Pipenv:
```bash
   pipenv install

3. Activate the virtual eniviroment:
```bash
   pipenv shell

4. Create the database tables:
```bash
   alembic upgrade head

5. Run the CLI with:
```bash
   python main.py

- You’ll see the main menu with options to manage Students, Courses, and Enrollments.


## 📚 Menu Options

### 🧑‍🎓 Students Menu
- **List all students** – View all students currently in the database.  
- **Add a student** – Create a new student record.  
- **Update student information** – Modify a student’s details (e.g., name, email).  
- **Delete a student** – Remove a student from the system.  
- **Back to main menu** – Return to the main menu.  

---

### 📘 Courses Menu
- **List all courses** – View all available courses.  
- **Add a course** – Create a new course.  
- **Update course information** – Modify a course’s details (e.g., title, description).  
- **Delete a course** – Remove a course from the system.  
- **Back to main menu** – Return to the main menu.  

---

### 📝 Enrollments Menu
- **List all enrollments** – View all student-course enrollments.  
- **Enroll student in course** – Assign a student to a course.  
  - When prompted, student and course options are shown for easier selection.  
- **Remove enrollment** – Unenroll a student from a course.  
- **Back to main menu** – Return to the main menu.  

## 🛠️ Technologies Used

- **Python 3.8+**  
- **SQLAlchemy** – ORM for database interactions  
- **Alembic** – Database migrations  
- **Click** – CLI creation  
- **Tabulate** – Nicely formatted CLI tables  
- **python-dotenv** – Manage environment variables  

## Project Structure
courseflow/
│── cli/
│   └── interface.py        # CLI menus and interface
│
│── db/
│   └── setup.py            # Database setup
│
│── models/
│   ├── student.py          # Student ORM model
│   ├── course.py           # Course ORM model
│   └── enrollment.py       # Enrollment ORM model
│
│── migrations/             # Alembic migration files
│   ├── versions/           # Versioned migration scripts
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
│── .venv/                  # Virtual environment
│── .env                    # Environment variables
│── alembic.ini             # Alembic configuration
│── courseflow.db           # SQLite database
│── inspect_db.py           # Utility to inspect DB tables
│── main.py                 # Entry point for CLI
│── Pipfile                 # Dependencies
│── Pipfile.lock            # Dependency lock file
│── README.md               # Documentation

## ✨ Features

- Manage students, courses, and enrollments directly from the CLI.  
- Database persistence using SQLite.  
- Schema management with Alembic migrations.  
- Clear, user-friendly CLI menus.  

## License
© 2025 Mike Muteithia — Moringa School.