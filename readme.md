# School Management System

This is a Django-based school management system that allows students, lecturers, administrators, and clinic staff to manage various academic and administrative tasks within a school environment. The system facilitates viewing results, generating timetables, registering courses, managing medical records, and more.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features

### Admin
- Manage students, lecturers, and clinic staff records.
- View and manage courses.
- View student results and medical records.

### Lecturer
- View courses they are teaching and the list of registered students.
- Input grades for students.
- Generate exam timetables.

### Student
- View personal exam results.
- Generate a course timetable based on registered courses.
- View and update personal profile information.

### Clinic Staff
- View and update student medical records.

## Technologies

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default for Django, easily replaceable with PostgreSQL or MySQL)
- **Other Tools**: Django Admin, Django Groups and Permissions

## Installation

### Prerequisites

Ensure you have the following installed on your local development environment:

- Python (>= 3.8)
- Django (>= 3.2)
- Git

### Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/school-management-system.git
    cd school-management-system
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    Run migrations to set up the database schema.

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (admin account):**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create your admin credentials.

6. **Run the server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open a browser and go to `http://127.0.0.1:8000` to access the system.

    You can access the Django admin at `http://127.0.0.1:8000/admin` using the superuser credentials you created.

## Usage

- **Admin**: Login to the admin dashboard to manage users, courses, results, and medical records.
- **Lecturer**: Login to view the list of students registered for your courses and input grades.
- **Student**: View your results, generate your timetable, and update your profile.
- **Clinic Staff**: View and update student medical records.

## Project Structure

```plaintext
school-management-system/
│
├── school_management/             # Main Django app
│   ├── migrations/                # Database migrations
│   ├── templates/                 # HTML templates
│   ├── static/                    # Static files (CSS, JS, images)
│   ├── models.py                  # Database models
│   ├── views.py                   # Views handling requests and responses
│   ├── urls.py                    # URL routing
│   └── forms.py                   # Forms for user input
│
├── manage.py                      # Django management script
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
