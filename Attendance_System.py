class Student:
    def __init__(self, roll_no, name):
        self.__roll_no = roll_no
        self.__name = name
        self.__present_days = 0

    def get_roll(self):       return self.__roll_no

    def get_name(self):
        return self.__name

    def get_present_days(self):
        return self.__present_days

    def mark_present(self):
        self.__present_days += 1

    def calculate_percentage(self, total_days):
        if total_days == 0:
            return 0
        return round((self.__present_days / total_days) * 100, 2)

class AttendanceSystem:
    def __init__(self):
        self.students = []
        self.total_days = 0

    def add_student(self, roll, name):
        self.students.append(Student(roll, name))
        print("Student Added Successfully!")

    def mark_attendance(self, roll):
        found = False
        for s in self.students:
            if s.get_roll() == roll:
                s.mark_present()
                found = True
        
        if found:
            self.total_days += 1
            print("Attendance Marked!")
        else:
            print("Student Not Found!")

    def view_attendance(self):
        if not self.students:
            print("No Students Available!")
            return

        print("\n----- Attendance Report -----")
        print(f"Total Working Days: {self.total_days}\n")
        print("Roll  Name     Present  Percentage  Status")

        for s in self.students:
            percent = s.calculate_percentage(self.total_days)
            status = "DEFAULTER" if percent < 75 else "OK"
            print(f"{s.get_roll()}      {s.get_name()}        {s.get_present_days()}       {percent}%     {status}")

    def search_student(self, roll):
        for s in self.students:
            if s.get_roll() == roll:
                percent = s.calculate_percentage(self.total_days)
                status = "DEFAULTER" if percent < 75 else "OK"
                print("\n--- Student Found ---")
                print("Roll No:", s.get_roll())
                print("Name:", s.get_name())
                print("Present Days:", s.get_present_days())
                print("Attendance %:", percent)
                print("Status:", status)
                return
        print("Student Not Found!")

system = AttendanceSystem()
while True:
    print("\n===== Attendance Recorder System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        roll = input("Roll No: ")
        name = input("Name: ")
        system.add_student(roll, name)

    elif choice == '2':
        roll = input("Enter Roll No: ")
        system.mark_attendance(roll)

    elif choice == '3':
        system.view_attendance()

    elif choice == '4':
        roll = input("Enter Roll No: ")
        system.search_student(roll)

    elif choice == '5':
        print("Exited from the program")
        break

    else:
        print("Invalid choice! Try again.")
