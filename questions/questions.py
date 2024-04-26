"""Balancing of paranthesis"""
from structures import Stack


def checkParanthesis(lst: list) -> bool:
    """:returns Boolean whether the paranthesis is balanced or not"""
    stack = Stack()
    for val in lst:
        # print(val,end=" ")
        if val in ("(", "{", "<", "["):
            stack.push(val)
        elif val in (")", "}", ">", "]"):
            # in case the stack is empty, then straight away False
            if stack.isEmpty():
                return False
            elif val == ")":
                if stack.peek() == "(":
                    stack.pop()
                else:
                    print("Expected (, but got {0}".format(stack.peek()))
                    return False
            elif val == "}":
                if stack.peek() == "{":
                    stack.pop()
                else:
                    print("Expected {, but got {0}".format(stack.peek()))
                    return False
            elif val == ">":
                if stack.peek() == "<":
                    stack.pop()
                else:
                    print("Expected <, but got {0}".format(stack.peek()))
                    return False
            elif val == "]":
                if stack.peek() == "[":
                    stack.pop()
                else:
                    print("Expected [, but got {0}".format(stack.peek()))
                    return False
    if stack.isEmpty():
        # If balanced the stack should be empty
        return True
    else:
        return False
    # return True if stack.isEmpty() else False


def checkBalance(lst: list, dictionary: dict = {"<": ">", "{": "}", "(": ")", "[": "]"},
                 detailed: bool = False) -> bool:
    """
    :returns Boolean whether the paranthesis is balanced or not
    :type lst: list
    :type dictionary: dict default: {"<":">","{":"}","(":")","[":"]"}
    :type detailed: bool default: False
    """
    stack = Stack()
    reverseDict = dict()
    for x in dictionary.keys():
        reverseDict[dictionary[x]] = x
    for val in lst:
        # print(val,end=" ")
        if val in dictionary.keys():
            stack.push(val)
        elif val in dictionary.values():
            # in case the stack is empty, then straight away False
            if stack.isEmpty():
                if detailed:
                    print("Received closing entity before an opening entity")
                return False
            elif reverseDict[val] != stack.peek():
                if detailed:
                    print("Expected {0}, but got {1}".format(reverseDict[val], stack.peek()))
                return False
            elif reverseDict[val] == stack.peek():
                stack.pop()
    if stack.isEmpty():
        return True
    else:
        if detailed:
            print("There are still open entities which need to be closed")
        return False
    # return True if stack.isEmpty() else False
