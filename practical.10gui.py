
import tkinter as tk
from tkinter import messagebox

SIZE = 10
hash_table = [None] * SIZE


def insert():
    try:
        key = int(entry.get())
        index = key % SIZE

        if hash_table[index] is None:
            hash_table[index] = key
            messagebox.showinfo("Success", "Element inserted!")
            entry.delete(0, tk.END)
            display()
        else:
            messagebox.showerror("Error", "Collision occurred!")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")


def delete():
    try:
        key = int(entry.get())
        index = key % SIZE

        if hash_table[index] == key:
            hash_table[index] = None
            messagebox.showinfo("Success", "Element deleted!")
            entry.delete(0, tk.END)
            display()
        else:
            messagebox.showerror("Error", "Element not found!")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")


def display():
    result.delete("1.0", tk.END)

    for i in range(SIZE):
        if hash_table[i] is None:
            result.insert(tk.END, f"Index {i} : Empty\n")
        else:
            result.insert(tk.END, f"Index {i} : {hash_table[i]}\n")


def clear():
    for i in range(SIZE):
        hash_table[i] = None

    display()
    entry.delete(0, tk.END)


# Main Window
root = tk.Tk()
root.title("Hash Table")
root.geometry("450x500")

title = tk.Label(
    root,
    text="HASH TABLE",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

label = tk.Label(
    root,
    text="Enter Key:",
    font=("Arial", 13)
)
label.pack()

entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=20
)
entry.pack(pady=10)

insert_btn = tk.Button(
    root,
    text="INSERT",
    width=15,
    command=insert
)
insert_btn.pack(pady=5)

delete_btn = tk.Button(
    root,
    text="DELETE",
    width=15,
    command=delete
)
delete_btn.pack(pady=5)

display_btn = tk.Button(
    root,
    text="TRAVERSAL / DISPLAY",
    width=20,
    command=display
)
display_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="CLEAR",
    width=15,
    command=clear
)
clear_btn.pack(pady=5)

result = tk.Text(
    root,
    height=12,
    width=35,
    font=("Arial", 12)
)
result.pack(pady=15)

display()

root.mainloop()

