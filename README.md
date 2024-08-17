# Django ERP System

This is a Django-based ERP (Enterprise Resource Planning) system for managing administration, faculties, courses, enrollment, and evaluation operations.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Administration**: Manage departments, degree levels, semesters, and degrees.
- **Faculties**: Manage professors and their courses.
- **Courses**: Manage courses, course dependencies, and occurrences.
- **Enrollment**: Manage student enrollments in degrees and courses.
- **Evaluation**: Manage course evaluations and grades.

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL

### Setup Instructions
1. **Clone the repository:**
    ```bash
    git clone https://github.com/saurabh228/IIITN-ERP-BackEnd.git
    cd IIITN-ERP-BackEnd
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv erpenv
    source erpenv/bin/activate  # On Windows use `erpenv\Scripts\activate`
    ```
    Make sure to select the virtual environment as the python interpreter in your IDE

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL database:**
    - Create a database named `academix` (or your preferred name).
    - Create a role with password and give required privileges 
    - Update the `DATABASES` setting in `erpbackend/settings.py` with your database credentials.

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Open the server in your web browser:**
    - Navigate to `http://127.0.0.1:8000/admin` to access the admin panel.

## Usage
1. **Access the admin panel:**
    - Log in with the superuser credentials you created.
    - Manage departments, degree levels, semesters, degrees, professors, courses, enrollments, and evaluations.

2. **API Endpoints:**
    - Use the API documentation at `http://127.0.0.1:8000/swagger/` to interact with the API endpoints using Postman or any other API client.

## API Documentation
API documentation is available at `http://127.0.0.1:8000/swagger/` once the server is running. You can use this documentation to explore and test the API endpoints.

## Contributing
1. **Fork the repository.**
2. **Create a new branch:**
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes and commit them:**
    ```bash
    git commit -m "Add some feature"
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature/your-feature-name
    ```
5. **Open a pull request.**


