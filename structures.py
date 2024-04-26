from collections import deque

# class LinkedinList():
#     class Node():
#         def __init__(self, value):
#             self.value = value
#             self.left = None
#             self.right = None
#     def __init__(self):
#         self.root = None
#     def __init__(self, head: Node):
#         self. root = head
#     def _insertNode(root, NewNode):
#         pass
#
#     def insertNode(self, NewNode:Node ):
#         if self.root == None:
#             self.root = NewNode
#         else:
#             self._insertNode(self.root,NewNode)

# class BinaryTree:
#     class BTNode:
#         def __init__(self):
#
#     def __init__(self):
#         self.root = None
#     def insertNode

# class Array:
#     def __init__(self):
#         self.self.list()
#     def append(self):
#         self.list
class BNode(object):
    def __init__(self, value=None):
        """ Initializes a node with value provided"""
        self.value = value
        self.left = None
        self.right = None

    def addLeft(self, otherNode: object):
        """Adds the other BNode to current node"""
        if type(otherNode) != BNode:
            raise Exception("Invalid datatype, \nExpected Binary Node, got something else")
        else:
            self.left = otherNode

    def addRight(self, otherNode: object):
        """Adds another Bnode to the right of the current object"""
        if type(otherNode) == BNode:
            raise Exception("Invalid datatype, \nExpected Binary Node, got something else")
        else:
            self.right(otherNode)


class BTree():
    def __init__(self):
        self.root = None

    def addNode(self, Node: BNode):
        """Add node to Balanced Binary tree"""
        if type(Node) != BNode:
            raise Exception("Invalid datatype, \nExpected Binary Node, got something else")
        elif self.root == None:
            self.root = Node
        elif self.value > Node.value:
            self.addNode()


class Stack():
    """Stack is dynamic linear data structure which implements LIFO, Last in First Out"""

    def __init__(self) -> None:
        """Initializes an empty stack i.e. size = 0"""
        self.lst = list()
        self.size = 0

    def getSize(self) -> int:
        return self.size

    def push(self, other: object) -> None:
        """Pushes the element onto the top of the stack"""
        self.lst.append(other)
        self.size += 1

    def pop(self) -> object:
        """Modifies the stack and :returns the element on the top of the stack"""
        if self.isEmpty():
            print("Underflow condition")
            print("Empty stack, nothing to pop")
            return None
        else:
            self.size -= 1
            return self.lst.pop()

    def peek(self):
        """":returns item on the top of the stack without modifying the stack"""
        if self.getSize() == 0:
            print("Empty Stack, no element on the top")
            return None
        else:
            return self.lst[-1]

    def isEmpty(self):
        """:returns whether the stack is empty ot not"""
        return True if self.getSize() == 0 else False

    def topElement(self):
        """":returns item on the top of the stack without modifying the stack\n Same as peek function"""
        return self.peek()

    def getStackStatus(self):
        """prints the status of the stack with length and the element on the top."""
        print("Length of the stack is {0}\n With element on the top as {1}".format({0: self.getSize(), 1: self.peek()}))

class Queue():
    """Queue is a dynamic linear data structure which implements the FIFO First In First Out
    \n **Desired features and Time Complexty**\n
    \n\tEnqueue -> O(1)
    \n\tDequeue -> O(1)
    \n\tFront -> O(1)
    \n\tRear _> O(1)
    """
    def __init__(self):
        """Using the collections.deque we can achieve the desired results"""
        self._queue = deque()

    def enqueue(self, other: object) -> None:
        """Adds an element to the queue at the reae end\n :inplace = True"""
        self._queue.append(other)

    def getSize(self):
        """:returns size of the queue"""
        return len(self._queue)

    def isEmpty(self):
        """:returns whether the queue is empty or not"""
        return True if self.getSize() == 0 else False

    def dequeue(self):
        """Removes an element from the front of the queue\n :inplace= True"""
        if self.isEmpty():
            raise Exception("Empty Queue, cannot remove element")
        else:
            self._queue.popleft()

    def front(self):
        """:returns the element present at the front of the queue\n This is the first element removed from the queue
        when dequeue() method is run"""
        if self.isEmpty():
            print("Empty queue")
            return None
        else:
            return self._queue[0]

    def rear(self):
        """:returns the element present at the rear end of the queue \n This is the last element added to the queue
        which was added when enqueue(other) was run"""
        if self.isEmpty():
            print("Empty queue")
            return None
        else:
            return self._queue[-1]

    def __str__(self):
        if self.isEmpty():
            return None
        else:
            return str(self._queue)




''' Array based implementation
    # Drawback: Enqueue and Dequeue methods implemented take O(n) instead of O(1)
    # Commented out for this purpose
    def __init__(self):
        self.queue = list()

    def enqueue(self, other: object)-> None:
        """Adds an element at the rear end of the queue"""
        self.queue.append(other)

    def getSize(self):
        """:returns length of the queue"""
        return len(self.queue)

    def isEmpty(self):
        """:returns True if the queue is empty"""
        return  True if self.getSize() == 0 else False

    def dequeue(self):
        """Removes the element at the front of the queue
        :raises Exception if the queue is empty"""
        if self.isEmpty():
            raise Exception("Empty Queue, undeflow condition")
        else:
            self.queue.pop(0)

    def rear(self):
        """;:returns the element at the end\nThis is the latest element added to the queue"""
        return self.queue[-1]

    def front(self):
        """:returns the front element of the queue\n This is the next element which will be removed"""
        return self.queue[0]
'''