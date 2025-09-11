class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    """Singly linked list with basic operations."""
    def __init__(self):
        self.head = None  # Start with an empty list

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, new node becomes the head
            self.head = new_node
            return
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        # Set the next pointer of the last node to the new node
        current.next = new_node

    def delete_value(self, value):
        """Delete the first node with the specified value."""
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev is None:
                    # Deleting the head node: update head pointer
                    self.head = current.next
                else:
                    # Bypass the current node by updating the previous node's next pointer
                    prev.next = current.next
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def traverse(self):
        """Traverse the list and return a list of node values."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next  # Move to the next node
        return elements

def main():
    print("Singly Linked List Demo")
    ll = LinkedList()
    while True:
        print("\nChoose operation:")
        print("1. Insert at end")
        print("2. Delete value")
        print("3. Traverse")
        print("4. Exit")
        choice = input("Enter option (1-4): ").strip()
        if choice == "1":
            value = input("Enter value to insert at end: ")
            ll.insert_at_end(value)
            print(f"Inserted {value} at end.")
        elif choice == "2":
            value = input("Enter value to delete: ")
            deleted = ll.delete_value(value)
            if deleted:
                print(f"Deleted {value} from list.")
            else:
                print(f"Value {value} not found in list.")
        elif choice == "3":
            elements = ll.traverse()
            print("Current list:", elements)
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

