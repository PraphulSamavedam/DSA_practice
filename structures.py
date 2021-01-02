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
    """Stack is dynamic data structure which implements LIFO, Last in First Out"""

    def __init__(self) -> None:
        """Initializes an empty stack i.e. size = 0"""
        self.lst = list()
        self.size = 0

    def getSize(self) -> int:
        return self.size

    def push(self, object) -> None:
        """Pushes the element onto the top of the stack"""
        self.lst.append(object)
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
