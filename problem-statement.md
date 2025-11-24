# Attendance Recorder System - Problem Statement

## Overview

Design and implement a simple, menu‑driven **Attendance Recorder System** using Python and object‑oriented programming.

## Objectives

The system should:

- Store student details (roll number, name, and number of days present).
- Allow the user to add new students to the system.
- Allow the user to mark a student as present by entering their roll number.
- Keep track of the total working days on which attendance has been recorded.
- Display a comprehensive attendance report for all students, showing:
  - Roll number
  - Name
  - Number of present days
  - Attendance percentage
  - Status (OK / DEFAULTER)
- Allow searching and displaying the attendance details of a single student by roll number.
- Run continuously as a menu-driven application until the user chooses to exit.

## Status Determination

A student is classified as:
- **OK**: Attendance percentage ≥ 75%
- **DEFAULTER**: Attendance percentage < 75%

## Key Features

1. **Object-Oriented Design**: Uses two main classes:
   - `Student`: Represents individual student records
   - `AttendanceSystem`: Manages the overall system and all students

2. **Data Encapsulation**: Student data is kept private using name mangling.

3. **User-Friendly Interface**: Simple text-based menu for easy interaction.

4. **Real-time Reporting**: View attendance reports and search for individual students at any time.

## Technical Requirements

- Language: Python 3.x
- Paradigm: Object-Oriented Programming (OOP)
- Interface: Command-line (CLI) menu-driven application
- Data Structure: Lists to store student objects
