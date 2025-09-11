class Node:
    """
    Node class for Binary Search Tree.

    Attributes:
        data (int): The value stored in the node.
        left (Node): Reference to the left child node.
        right (Node): Reference to the right child node.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree implementation.

    Methods:
        insert(value): Insert a value into the BST.
        search(value): Search for a value in the BST. Returns True if found, else False.
        inorder_traversal(): Return a list of values in inorder traversal.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Args:
            value (int): The value to insert.
        """
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.data:
                node.left = _insert(node.left, value)
            elif value > node.data:
                node.right = _insert(node.right, value)
            # If value == node.data, do not insert duplicates
            return node
        self.root = _insert(self.root, value)

    def search(self, value):
        """
        Search for a value in the BST.

        Args:
            value (int): The value to search for.

        Returns:
            bool: True if value is found, False otherwise.
        """
        def _search(node, value):
            if node is None:
                return False
            if value == node.data:
                return True
            elif value < node.data:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def inorder_traversal(self):
        """
        Perform inorder traversal of the BST.

        Returns:
            list: List of values in inorder.
        """
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)
        _inorder(self.root)
        return result

def main():
    print("Binary Search Tree Demo")
    bst = BST()
    # Ask user to enter input values
    values = input("Enter integers to insert into BST (space-separated): ").strip()
    if values:
        for val in values.split():
            try:
                bst.insert(int(val))
            except ValueError:
                print(f"Invalid input ignored: {val}")

    while True:
        print("\nChoose operation:")
        print("1. Insert value")
        print("2. Search value")
        print("3. Inorder traversal")
        print("4. Exit")
        choice = input("Enter option (1-4): ").strip()
        if choice == "1":
            val = input("Enter integer to insert: ").strip()
            try:
                bst.insert(int(val))
                print(f"Inserted {val} into BST.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "2":
            val = input("Enter integer to search: ").strip()
            try:
                found = bst.search(int(val))
                if found:
                    print(f"Value {val} found in BST.")
                else:
                    print(f"Value {val} NOT found in BST.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "3":
            traversal = bst.inorder_traversal()
            print("Inorder traversal:", traversal)
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

