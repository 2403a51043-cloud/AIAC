
class QueueList:
    """Queue implementation using Python list."""

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add item to the end of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._items) == 0

    def __str__(self):
        return f"QueueList({self._items})"


# Performance Review (AI-generated)
review = """
Performance Review:
The above Queue implementation uses a Python list. While enqueue (append) is O(1), dequeue (pop(0)) is O(n) because all elements must be shifted after removing the first item. For better performance, especially with many dequeue operations, use collections.deque, which provides O(1) time complexity for both enqueue and dequeue operations.
"""

# Optimized Queue using collections.deque
from collections import deque

class QueueDeque:
    """Queue implementation using collections.deque."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add item to the end of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._items) == 0

    def __str__(self):
        return f"QueueDeque({list(self._items)})"


def main():
    print("Queue Implementation Demo")
    print("1. Use Queue with Python list")
    print("2. Use Queue with collections.deque (recommended for performance)")
    choice = input("Select queue implementation (1 or 2): ").strip()

    if choice == "1":
        queue = QueueList()
        print("\n[Performance Review]")
        print(review)
    elif choice == "2":
        queue = QueueDeque()
    else:
        print("Invalid choice.")
        return

    while True:
        print("\nCurrent queue:", queue)
        print("Choose operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Check if empty")
        print("4. Exit")
        op = input("Enter option (1-4): ").strip()

        if op == "1":
            value = input("Enter value to enqueue: ")
            queue.enqueue(value)
            print(f"Enqueued: {value}")
        elif op == "2":
            try:
                item = queue.dequeue()
                print(f"Dequeued: {item}")
            except IndexError as e:
                print("Error:", e)
        elif op == "3":
            print("Queue is empty?" , queue.is_empty())
        elif op == "4":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

