# implementing class array with method insert, delete and get.
class Array:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            self.data.pop(index)
        else:
            raise IndexError("Index is out of range")

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index is out of range")

    def __str__(self):
        return str(self.data)


#Creating aray object and calling available methods 
arr = Array()
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
print("Array:", arr)
print("Access index 1:", arr.get(1))
arr.delete(1)
print("After deletion:", arr)


#Implementing matrix as lists of lists.
# with methods insert, delete and get.
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def insert(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Row or column is out of range")

    def delete(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = 0
        else:
            raise IndexError("Row or column is out of range")

    def get(self, row, col):
        """Access a value at a specific row and column."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Row or column is out of range")

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])


# Creating matrix object and calling available methods
# with parameters.
matrix = Matrix(3, 3)
matrix.insert(0, 0, 1)
matrix.insert(1, 1, 2)
matrix.insert(2, 2, 3)
print("Matrix:")
print(matrix)
print("Access (1, 1):", matrix.get(1, 1))
matrix.delete(1, 1)
print("After deletion:")
print(matrix)


#implementing slack with method push, pop, peek and is empty.
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("Error! Popping from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("Error! Peeking from empty stack")

    def is_empty(self):
        return len(self.data) == 0


# Creating Stack object and calling methods push and pop.
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack:", stack)
print("Pop:", stack.pop())
print("After pop:", stack)
print("Peek:", stack.peek())


#Implementing Queue with methods enqueue and Dequeue
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        """Add a value to the queue."""
        self.data.append(value)

    def dequeue(self):
        """Remove a value from the queue."""
        if not self.is_empty():
            return self.data.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.data[0]
        else:
            raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.data) == 0


#Creating queue class object and performing
#enqueue and dequeue.
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue:", queue)
print("Dequeue:", queue.dequeue())
print("After dequeue:", queue)
print("Peek:", queue.peek())


#Implementing Single Linked list with Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Contains method insert at head, tail, delete and search
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)


#Created singly linked list object and inserting at both head and tail.
sll = SingleLinkedList()
sll.insert_at_head(10)
sll.insert_at_tail(20)
sll.insert_at_tail(30)
print("Linked List:", sll)
sll.delete(20)
print("After deletion:", sll)
print("Search for 30:", sll.search(30))


#Implementing Rooted tree with Tree Node.
#Tree node contains method add child and Rooted tree contains
# metho traverse.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        """Add a child node."""
        self.children.append(child)

    def __str__(self):
        return str(self.data)


class RootedTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def traverse(self, node=None):
        """Traverse the tree starting from the given node."""
        if node is None:
            node = self.root
        print(node)
        for child in node.children:
            self.traverse(child)


#creating rooted tree object with 3 tree nodes.
tree = RootedTree(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child1.add_child(TreeNode(4))
child1.add_child(TreeNode(5))
tree.root.add_child(child1)
tree.root.add_child(child2)
print("Tree traversal:")
tree.traverse()