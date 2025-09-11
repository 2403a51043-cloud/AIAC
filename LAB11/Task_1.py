
class Stack:
    """A simple Stack implementation using a Python list.

    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item of the stack.
        peek(): Return the top item without removing it.
        is_empty(): Check if the stack is empty.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """Push an item onto the top of the stack.

        Args:
            item: The item to be added.
        """
        self._items.append(item)

    def pop(self):
        """Remove and return the top item of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item of the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0


# Test stack operations using sample data
if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.is_empty())  # True

    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element (peek):", stack.peek())  # 30

    # Pop elements
    print("Popped:", stack.pop())  # 30
    print("Popped:", stack.pop())  # 20
    print("Is stack empty?", stack.is_empty())  # False

    print("Popped:", stack.pop())  # 10
    print("Is stack empty?", stack.is_empty())  # True

