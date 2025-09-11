class Graph:
    """
    Graph implementation using an adjacency list.
    Supports BFS and DFS traversals.
    """
    def __init__(self):
        # The adjacency list is a dictionary where keys are nodes and values are lists of neighbors
        self.adj_list = {}

    def add_edge(self, u, v):
        """
        Add an edge from node u to node v (undirected by default).
        """
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # For undirected graph

    def bfs(self, start):
        """
        Perform Breadth-First Search (BFS) traversal from the start node.
        Returns the order of traversal as a list.
        """
        from collections import deque
        visited = set()  # To keep track of visited nodes
        queue = deque([start])  # Queue for BFS
        order = []

        while queue:
            node = queue.popleft()  # Dequeue a node
            if node not in visited:
                # Visit the node and add to result
                visited.add(node)
                order.append(node)
                # Enqueue all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order

    def dfs_iterative(self, start):
        """
        Perform Depth-First Search (DFS) traversal (iterative) from the start node.
        Returns the order of traversal as a list.
        """
        visited = set()
        stack = [start]  # Stack for DFS
        order = []

        while stack:
            node = stack.pop()  # Pop a node from the stack
            if node not in visited:
                # Visit the node and add to result
                visited.add(node)
                order.append(node)
                # Add all unvisited neighbors to the stack
                # Reversed to maintain order similar to recursive DFS
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def dfs_recursive(self, start):
        """
        Perform Depth-First Search (DFS) traversal (recursive) from the start node.
        Returns the order of traversal as a list.
        """
        order = []
        visited = set()

        def dfs(node):
            if node not in visited:
                # Visit the node and add to result
                visited.add(node)
                order.append(node)
                # Recursively visit all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    dfs(neighbor)
        dfs(start)
        return order

    def display(self):
        """
        Display the adjacency list of the graph.
        """
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")

def main():
    print("Graph Representation and Traversal Demo")
    g = Graph()
    print("Enter edges (as pairs, e.g., 'A B'). Type 'done' to finish:")
    while True:
        edge = input("Edge: ").strip()
        if edge.lower() == 'done':
            break
        parts = edge.split()
        if len(parts) != 2:
            print("Please enter exactly two nodes separated by space.")
            continue
        u, v = parts
        g.add_edge(u, v)
    print("\nAdjacency List of the Graph:")
    g.display()

    while True:
        print("\nChoose traversal method:")
        print("1. BFS (Breadth-First Search)")
        print("2. DFS (Iterative)")
        print("3. DFS (Recursive)")
        print("4. Compare DFS Iterative vs Recursive")
        print("5. Exit")
        choice = input("Enter option (1-5): ").strip()
        if choice == "1":
            start = input("Enter start node for BFS: ").strip()
            order = g.bfs(start)
            print("BFS Traversal Order:", order)
        elif choice == "2":
            start = input("Enter start node for DFS (Iterative): ").strip()
            order = g.dfs_iterative(start)
            print("DFS Iterative Traversal Order:", order)
        elif choice == "3":
            start = input("Enter start node for DFS (Recursive): ").strip()
            order = g.dfs_recursive(start)
            print("DFS Recursive Traversal Order:", order)
        elif choice == "4":
            start = input("Enter start node for DFS comparison: ").strip()
            order_iter = g.dfs_iterative(start)
            order_rec = g.dfs_recursive(start)
            print("DFS Iterative Order:", order_iter)
            print("DFS Recursive Order:", order_rec)
            if order_iter == order_rec:
                print("Both DFS methods produce the same order.")
            else:
                print("DFS methods produce different orders (due to neighbor order or graph structure).")
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
