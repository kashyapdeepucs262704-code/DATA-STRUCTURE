import tkinter as tk
from tkinter import messagebox


class Student:
    def __init__(self, roll_no, name, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.marks = marks


students = {}


def clear_fields():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)


def create_student():
    roll_no = roll_entry.get()
    name = name_entry.get()
    course = course_entry.get()
    marks = marks_entry.get()

    if roll_no == "" or name == "" or course == "" or marks == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    if roll_no in students:
        messagebox.showerror("Error", "Student already exists")
        return

    try:
        marks = float(marks)
    except ValueError:
        messagebox.showerror("Error", "Marks must be a number")
        return

    students[roll_no] = Student(
        roll_no,
        name,
        course,
        marks
    )

    messagebox.showinfo("Success", "Student created successfully")
    clear_fields()


def update_student():
    roll_no = roll_entry.get()

    if roll_no not in students:
        messagebox.showerror("Error", "Student not found")
        return

    name = name_entry.get()
    course = course_entry.get()
    marks = marks_entry.get()

    if name == "" or course == "" or marks == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    try:
        marks = float(marks)
    except ValueError:
        messagebox.showerror("Error", "Marks must be a number")
        return

    students[roll_no].name = name
    students[roll_no].course = course
    students[roll_no].marks = marks

    messagebox.showinfo("Success", "Student updated successfully")
    clear_fields()


def delete_student():
    roll_no = roll_entry.get()

    if roll_no not in students:
        messagebox.showerror("Error", "Student not found")
        return

    del students[roll_no]

    messagebox.showinfo("Success", "Student deleted successfully")
    clear_fields()


def display_students():
    display_box.delete("1.0", tk.END)

    if not students:
        display_box.insert(tk.END, "No student records found.")
        return

    for student in students.values():
        display_box.insert(
            tk.END,
            "Roll No : " + student.roll_no + "\n"
            "Name    : " + student.name + "\n"
            "Course  : " + student.course + "\n"
            "Marks   : " + str(student.marks) + "\n"
            "-----------------------------\n"
        )


def search_student():
    roll_no = roll_entry.get()

    if roll_no not in students:
        messagebox.showerror("Error", "Student not found")
        return

    student = students[roll_no]

    name_entry.delete(0, tk.END)
    name_entry.insert(0, student.name)

    course_entry.delete(0, tk.END)
    course_entry.insert(0, student.course)

    marks_entry.delete(0, tk.END)
    marks_entry.insert(0, student.marks)


root = tk.Tk()
root.title("Student ADT")
root.geometry("600x550")


title_label = tk.Label(
    root,
    text="STUDENT ABSTRACT DATA TYPE",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=15)


frame = tk.Frame(root)
frame.pack()


tk.Label(frame, text="Roll No:", font=("Arial", 12)).grid(
    row=0, column=0, padx=10, pady=8
)

roll_entry = tk.Entry(frame, width=30)
roll_entry.grid(row=0, column=1)


tk.Label(frame, text="Name:", font=("Arial", 12)).grid(
    row=1, column=0, padx=10, pady=8
)

name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=1, column=1)


tk.Label(frame, text="Course:", font=("Arial", 12)).grid(
    row=2, column=0, padx=10, pady=8
)

course_entry = tk.Entry(frame, width=30)
course_entry.grid(row=2, column=1)


tk.Label(frame, text="Marks:", font=("Arial", 12)).grid(
    row=3, column=0, padx=10, pady=8
)

marks_entry = tk.Entry(frame, width=30)
marks_entry.grid(row=3, column=1)


button_frame = tk.Frame(root)
button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="Create",
    width=12,
    command=create_student
).grid(row=0, column=0, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Search",
    width=12,
    command=search_student
).grid(row=0, column=1, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Update",
    width=12,
    command=update_student
).grid(row=0, column=2, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Delete",
    width=12,
    command=delete_student
).grid(row=1, column=0, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Display",
    width=12,
    command=display_students
).grid(row=1, column=1, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_fields
).grid(row=1, column=2, padx=5, pady=5)


tk.Label(
    root,
    text="Student Records",
    font=("Arial", 14, "bold")
).pack(pady=5)


display_box = tk.Text(
    root,
    width=65,
    height=12
)

display_box.pack(pady=5)


root.mainloop()
