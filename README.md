# Homework Manager

The **Homework Manager** is a Python-based application designed to help teachers efficiently track and manage students' homework statuses. This tool provides a simple interface for teachers to log in, search for students by name and ID, and view or update their homework status. Data is stored in CSV files, making the application lightweight and easy to manage.

---

## Features

- **Teacher Login**: Verifies the teacher’s credentials with a simple username and password system.
- **Student Search**: Allows teachers to search for students by name and ID.
- **Homework Status Tracking**: Teachers can view and modify students' homework completion status.
- **Data Persistence**: Student and teacher data is stored in CSV files, ensuring the information remains saved between sessions.

---

## Prerequisites

To run the Homework Manager, ensure you have the following installed:
- Python 3.x
- `pyfiglet` library for styled text (`pip install pyfiglet`)
- `tabulate` library for table formatting (optional, not used in this version)

---

## File Structure

- **`student.py`**: Contains the `Student` class with methods for searching and updating student homework statuses.
- **`main.py`**: The main program that handles user interaction, including login, student search, and status updates.
- **`teacher.csv`**: CSV file containing teacher login credentials (username, password).
- **`student.csv`**: CSV file containing student data (name, ID, homework status).

---

## How It Works

### 1. **Teacher Login**
   - Upon starting the application, the teacher is prompted to log in by entering their username and password.
   - The login credentials are verified by checking against the `teacher.csv` file.

### 2. **Student Search**
   - After logging in, the teacher can search for a student by their name and ID.
   - The `Student.search_student()` method is used to check if the student exists in the `student.csv` file.

### 3. **Viewing Homework Status**
   - Once the student is found, the teacher can view the current homework status of the student.

### 4. **Updating Homework Status**
   - If necessary, the teacher can update the student’s homework status (e.g., from "Not Submitted" to "Completed").
   - The `Student.change_status()` method updates the student's status in the `student.csv` file.

---

## Code Breakdown

### `student.py`

The `Student` class includes three key methods:

- **`__init__(self, name, student_id)`**: Initializes a new student with their name and ID.
- **`search_student(file_name, name, student_id)`**: Searches for a student in a CSV file by name and ID.
- **`search_status(file_name, name, student_id)`**: Retrieves the current homework status of a student.
- **`change_status(file_name, name, student_id, new_status)`**: Updates the student's homework status in the CSV file.

### `main.py`

The main program handles the user interface:

- **`login()`**: Handles teacher login and validates credentials.
- **`students()`**: Prompts the teacher to input student details and checks if the student exists.
- **`data()`**: Displays the student's current homework status.
- **`change()`**: Prompts the teacher to update the student's homework status if necessary.

---

## How to Run

1. Clone or download the repository to your local machine.
2. Ensure the required CSV files (`teacher.csv` and `student.csv`) are populated with data.
3. Run the program using Python:

   ```bash
   python main.py

## Future Improvements
- Add more functionality for managing multiple students at once.
- Implement error handling for invalid inputs.
- Add a graphical user interface (GUI) for better user interaction.

