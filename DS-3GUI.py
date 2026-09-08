
import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")

        if position == 0:
            self.insert_at_beginning(data)
            return

        if self.head is None:
            raise IndexError("Position out of bounds.")

        new_node = Node(data)
        temp = self.head

        for _ in range(position - 1):
            if temp.next is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def delete_node_by_value(self, value):
        if self.head is None:
            raise ValueError("Linked List is empty.")

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        raise ValueError("Value not found.")

    def delete_node_by_index(self, position):
        if position < 0:
            raise IndexError("Index cannot be negative.")

        if self.head is None:
            raise ValueError("Linked List is empty.")

        if position == 0:
            self.head = self.head.next
            return

        temp = self.head

        for _ in range(position - 1):
            if temp.next is None:
                raise IndexError("Index out of bounds.")
            temp = temp.next

        if temp.next is None:
            raise IndexError("Index out of bounds.")

        temp.next = temp.next.next

    def display(self):
        values = []
        temp = self.head

        while temp:
            values.append(str(temp.data))
            temp = temp.next

        return " -> ".join(values) + (" -> None" if values else "Empty")


class LinkedListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Singly Linked List")
        self.root.geometry("650x500")
        self.root.resizable(False, False)

        self.linked_list = LinkedList()

        # Title
        title = tk.Label(
            root,
            text="Singly Linked List",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=15)

        # Data input
        data_frame = tk.Frame(root)
        data_frame.pack(pady=5)

        tk.Label(
            data_frame,
            text="Enter Data:",
            font=("Arial", 12)
        ).grid(row=0, column=0, padx=5)

        self.data_entry = tk.Entry(
            data_frame,
            font=("Arial", 12),
            width=15
        )
        self.data_entry.grid(row=0, column=1, padx=5)

        # Position input
        position_frame = tk.Frame(root)
        position_frame.pack(pady=5)

        tk.Label(
            position_frame,
            text="Position / Index:",
            font=("Arial", 12)
        ).grid(row=0, column=0, padx=5)

        self.position_entry = tk.Entry(
            position_frame,
            font=("Arial", 12),
            width=15
        )
        self.position_entry.grid(row=0, column=1, padx=5)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Insert Beginning",
            width=18,
            command=self.insert_beginning
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Insert End",
            width=18,
            command=self.insert_end
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Insert at Position",
            width=18,
            command=self.insert_position
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Delete by Value",
            width=18,
            command=self.delete_value
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Delete by Index",
            width=18,
            command=self.delete_index
        ).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Display List",
            width=18,
            command=self.display_list
        ).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=18,
            command=self.clear_list
        ).grid(row=3, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Exit",
            width=18,
            command=root.destroy
        ).grid(row=3, column=1, padx=5, pady=5)

        # Output label
        tk.Label(
            root,
            text="Linked List:",
            font=("Arial", 13, "bold")
        ).pack(pady=5)

        self.output = tk.Label(
            root,
            text="Empty",
            font=("Arial", 14, "bold"),
            relief="sunken",
            width=55,
            height=3,
            wraplength=550
        )
        self.output.pack(pady=10)

    def get_data(self):
        try:
            return int(self.data_entry.get())
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid integer."
            )
            return None

    def get_position(self):
        try:
            return int(self.position_entry.get())
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid position/index."
            )
            return None

    def insert_beginning(self):
        data = self.get_data()

        if data is not None:
            self.linked_list.insert_at_beginning(data)
            self.display_list()
            messagebox.showinfo(
                "Success",
                "Node inserted at beginning."
            )

    def insert_end(self):
        data = self.get_data()

        if data is not None:
            self.linked_list.insert_at_end(data)
            self.display_list()
            messagebox.showinfo(
                "Success",
                "Node inserted at end."
            )

    def insert_position(self):
        data = self.get_data()
        position = self.get_position()

        if data is not None and position is not None:
            try:
                self.linked_list.insert_at_position(
                    data,
                    position
                )
                self.display_list()

                messagebox.showinfo(
                    "Success",
                    f"Node inserted at position {position}."
                )

            except IndexError as e:
                messagebox.showerror(
                    "Error",
                    str(e)
                )

    def delete_value(self):
        data = self.get_data()

        if data is not None:
            try:
                self.linked_list.delete_node_by_value(data)
                self.display_list()

                messagebox.showinfo(
                    "Success",
                    f"Node with value {data} deleted."
                )

            except ValueError as e:
                messagebox.showerror(
                    "Error",
                    str(e)
                )

    def delete_index(self):
        position = self.get_position()

        if position is not None:
            try:
                self.linked_list.delete_node_by_index(
                    position
                )
                self.display_list()

                messagebox.showinfo(
                    "Success",
                    f"Node at index {position} deleted."
                )

            except (ValueError, IndexError) as e:
                messagebox.showerror(
                    "Error",
                    str(e)
                )

    def display_list(self):
        result = self.linked_list.display()
        self.output.config(text=result)

    def clear_list(self):
        self.linked_list.head = None
        self.output.config(text="Empty")

        self.data_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)

        messagebox.showinfo(
            "Clear",
            "Linked List has been cleared."
        )


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListGUI(root)
    root.mainloop()

