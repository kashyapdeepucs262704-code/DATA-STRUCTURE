class Student:
    def __init__(self, roll_no, name, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.marks = marks

    def display(self):
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Course  :", self.course)
        print("Marks   :", self.marks)
        print("-" * 30)


students = {}


def create_student():
    roll_no = input("Enter Roll No: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = Student(roll_no, name, course, marks)

    print("Student created successfully!")


def display_students():
    if not students:
        print("No student records found!")
        return

    print("\nStudent Records")
    print("=" * 30)

    for student in students.values():
        student.display()


def update_student():
    roll_no = input("Enter Roll No to update: ")

    if roll_no not in students:
        print("Student not found!")
        return

    student = students[roll_no]

    student.name = input("Enter New Name: ")
    student.course = input("Enter New Course: ")
    student.marks = float(input("Enter New Marks: "))

    print("Student updated successfully!")


def delete_student():
    roll_no = input("Enter Roll No to delete: ")

    if roll_no not in students:
        print("Student not found!")
        return

    del students[roll_no]

    print("Student deleted successfully!")


while True:

    print("\n========== STUDENT ADT ==========")
    print("1. Create Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
