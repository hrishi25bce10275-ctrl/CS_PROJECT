# Attendance Recorder System - Pseudocode

## Student Class

```
CLASS Student
    PRIVATE roll_no
    PRIVATE name
    PRIVATE present_days

    METHOD __init__(roll_no, name)
        SET self.roll_no = roll_no
        SET self.name = name
        SET self.present_days = 0

    METHOD get_roll()
        RETURN self.roll_no

    METHOD get_name()
        RETURN self.name

    METHOD get_present_days()
        RETURN self.present_days

    METHOD mark_present()
        INCREMENT self.present_days by 1

    METHOD calculate_percentage(total_days)
        IF total_days == 0
            RETURN 0
        ELSE
            percentage = (present_days / total_days) * 100
            ROUND percentage to 2 decimal places
            RETURN percentage
END CLASS
```

## AttendanceSystem Class

```
CLASS AttendanceSystem
    PUBLIC students (list)
    PUBLIC total_days (integer)

    METHOD __init__()
        CREATE empty list students
        SET total_days = 0

    METHOD add_student(roll, name)
        CREATE new Student object with roll and name
        APPEND it to students list
        PRINT "Student Added Successfully!"

    METHOD mark_attendance(roll)
        SET found = False
        FOR each student s in students
            IF s.get_roll() == roll
                CALL s.mark_present()
                SET found = True
        IF found is True
            INCREMENT total_days by 1
            PRINT "Attendance Marked!"
        ELSE
            PRINT "Student Not Found!"

    METHOD view_attendance()
        IF students list is empty
            PRINT "No Students Available!"
            RETURN

        PRINT header with title and total working days
        PRINT column headings: Roll, Name, Present, Percentage, Status

        FOR each student s in students
            percent = CALL s.calculate_percentage(total_days)
            IF percent < 75
                status = "DEFAULTER"
            ELSE
                status = "OK"
            PRINT row with: roll, name, present_days, percent, status

    METHOD search_student(roll)
        FOR each student s in students
            IF s.get_roll() == roll
                percent = CALL s.calculate_percentage(total_days)
                IF percent < 75
                    status = "DEFAULTER"
                ELSE
                    status = "OK"
                PRINT full details of that student
                PRINT roll, name, present days, percentage, status
                RETURN
        PRINT "Student Not Found!"
END CLASS
```

## Main Menu Loop

```
CREATE AttendanceSystem object called system

LOOP forever
    PRINT main menu:
        1. Add Student
        2. Mark Attendance
        3. View Attendance
        4. Search Student
        5. Exit

    READ choice from user

    IF choice == '1'
        READ roll from user
        READ name from user
        CALL system.add_student(roll, name)

    ELSE IF choice == '2'
        READ roll from user
        CALL system.mark_attendance(roll)

    ELSE IF choice == '3'
        CALL system.view_attendance()

    ELSE IF choice == '4'
        READ roll from user
        CALL system.search_student(roll)

    ELSE IF choice == '5'
        PRINT "Exited from the program"
        BREAK loop (exit program)

    ELSE
        PRINT "Invalid choice! Try again."
END LOOP
```

## Flow Chart Summary

```
START
  ↓
Create AttendanceSystem
  ↓
LOOP:
  Display Menu
  ↓
  Read Choice
  ↓
  IF choice == 1 → Add Student
  ↓
  IF choice == 2 → Mark Attendance
  ↓
  IF choice == 3 → View All Attendance
  ↓
  IF choice == 4 → Search Student
  ↓
  IF choice == 5 → Exit
  ↓
  ELSE → Show Invalid Message, Continue Loop
  ↓
END
```
