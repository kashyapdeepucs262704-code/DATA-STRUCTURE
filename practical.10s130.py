class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key):
        index = key % self.size
        self.table[index] = key
        print("Inserted:", key)

    def delete(self, key):
        index = key % self.size

        if self.table[index] == key:
            self.table[index] = None
            print("Deleted:", key)
        else:
            print("Key not found")

    def traverse(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(i, "->", self.table[i])


# Main program
size = int(input("Enter hash table size: "))

h = HashTable(size)

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Traverse")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        h.insert(key)

    elif choice == 2:
        key = int(input("Enter key to delete: "))
        h.delete(key)

    elif choice == 3:
        h.traverse()

    elif choice == 4:
        print("Program ended")
        break

    else:
        print("Invalid choice")
