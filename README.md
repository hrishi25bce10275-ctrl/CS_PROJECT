# Attendance Recorder System

## Author Information
- **Name:** Hrishi Upadhyay
- **Registration No.:** 25BCE10275
- **Institution:** VIT Bhopal, Computer Science & Engineering
- **Guide:** Prof. Shrishtika Raikwar

## Project Overview

The **Attendance Recorder System** is a Python-based console application designed to efficiently manage student attendance records. This system provides a user-friendly interface for educational institutions to track attendance, calculate attendance percentages, and automatically identify students who fall below the minimum attendance threshold (defaulters).

## Key Features

- **Add Students:** Register new students with roll number and name.
- **Mark Attendance:** Record daily attendance for registered students.
- **View Attendance Report:** Display comprehensive attendance data for all students with percentages and defaulter status.
- **Search Individual Records:** Query specific student attendance details by roll number.
- **Automatic Calculations:** Real-time attendance percentage calculation and defaulter identification.
- **Data Encapsulation:** Private attributes protect student data integrity.

## Problem Statement

Traditional paper-based attendance systems are prone to errors, data loss, and inconsistent record-keeping. This project addresses these challenges by providing a digital, automated solution that ensures accurate attendance tracking, reduces administrative overhead, and enables quick identification of students requiring intervention.

## Technologies & Tools Used

- **Language:** Python 3.x
- **Programming Paradigm:** Object-Oriented Programming (OOP)
- **Key Concepts:** Encapsulation, Classes, Methods, Data Structures (Lists)
- **IDE/Environment:** Any Python-compatible IDE (PyCharm, VSCode, etc.)

## Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- Basic knowledge of command-line interface

### Steps
1. Download or clone the project files.
2. Navigate to the project directory.
3. Run the program using:
   ```bash
   python attendance_recorder.py
   ```
4. Follow the on-screen menu prompts to interact with the system.

## File Organization

```
attendance_project/
│
├── attendance_recorder.py              # Main application code
├── README.md                           # Project overview (this file)
├── docs/
│   ├── documentation.md                # Detailed technical documentation
│   ├── statement.md                    # Problem statement
│   ├── workflow.png                    # Workflow diagram screenshot
│   ├── flowchart.png                   # System flowchart screenshot
│   └── screenshots/
│       ├── menu_display.png            # Main menu screenshot
│       ├── add_student_demo.png        # Add student operation screenshot
│       ├── attendance_report.png       # View attendance report screenshot
│       └── search_student_demo.png     # Search functionality screenshot
├── DESIGN.md                           # Architecture and design details
└── LICENSE                             # Project license (optional)
```

## Usage Guide

### Starting the Program
Run the Python file to display the main menu:
```
===== Attendance Recorder System =====
1. Add Student
2. Mark Attendance
3. View Attendance
4. Search Student
5. Exit
```

### Operations

**1. Add Student**
- Enter roll number and student name
- System confirms successful addition

**2. Mark Attendance**
- Provide roll number of the student
- System increments present days and total working days

**3. View Attendance**
- Displays attendance report for all students
- Shows: Roll, Name, Present Days, Attendance %, Status (OK/DEFAULTER)
- Defaulter: Students with attendance < 75%

**4. Search Student**
- Enter roll number to view individual attendance record
- Displays detailed information including attendance percentage and status

**5. Exit**
- Safely exit the program

## Workflow & Architecture

### System Flowchart
[See `docs/flowchart.png` - Uploaded workflow diagram showing system logic flow]

### Workflow Diagram
[See `docs/workflow.png` - Uploaded workflow diagram showing user interactions]

## Pseudo Code

Detailed pseudo code for all classes and methods is provided in the `documentation.md` file. Key algorithm includes:

```
Function calculate_attendance_percentage():
    IF total_days == 0:
        RETURN 0
    ELSE:
        RETURN (present_days / total_days) * 100 rounded to 2 decimals

Function mark_attendance(roll_number):
    SEARCH for student with matching roll_number
    IF found:
        INCREMENT student's present_days
        INCREMENT system's total_days
        DISPLAY "Attendance Marked!"
    ELSE:
        DISPLAY "Student Not Found!"

Function determine_status(attendance_percentage):
    IF attendance_percentage < 75:
        RETURN "DEFAULTER"
    ELSE:
        RETURN "OK"
```

## Detailed Documentation

For comprehensive technical documentation, including:
- Class-by-class implementation details
- Complete pseudo code for all methods
- Data flow diagrams
- Testing and validation procedures

Please refer to `docs/documentation.md`

## Screenshots

<img width="1920" height="1080" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/941abeaa-74d8-4d5e-ab99-70c2373dcebc" />
<img width="1920" height="1080" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/8ea90f42-e7d4-4a01-a230-96e72de34af2" />
<img width="1920" height="1080" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/37805baa-5820-43e2-8653-245165103e6a" />

- Main menu interface
- Student addition workflow
- Attendance report generation
- Individual student search results

## Testing & Validation

The system has been tested for:
<img width="1920" height="1080" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/54a2fbab-1513-4def-ace5-bf901ff14e70" />
<img width="1920" height="1080" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/fe124e25-5672-4764-8d98-f4fdf22354ef" />
- Correct student addition and retrieval
- Accurate attendance marking and percentage calculation
- Proper defaulter identification (< 75% attendance)
- Edge cases (zero total days, duplicate roll numbers, invalid inputs)
- Data encapsulation and privacy

## Key Design Patterns

- **Encapsulation:** Private attributes (`__roll_no`, `__name`, `__present_days`) protect data
- **Single Responsibility:** Each class handles specific functionality
- **Menu-Driven Interface:** User-friendly console interaction

## References

- Python Official Documentation: https://docs.python.org/3/
- Object-Oriented Programming Principles
- VIT Bhopal Project Guidelines
- Data Structure and Algorithm concepts

## Additional Notes

- The system uses a 75% attendance threshold for defaulter identification (customizable)
- All data is stored in memory during runtime; for persistence, database integration is recommended
- The system is designed for educational use and can be extended with database connectivity, GUI, or reporting features

## Support & Queries

For questions or clarifications regarding this project, please contact:
- **Student:** Hrishi Upadhyay (25BCE10275)
- **Guide:** Prof. Shrishtika Raikwar

---

**Project Submission Date:** November 2025
**Academic Year:** 2025-2026
**Course:** Computer Science & Engineering, VIT Bhopal
