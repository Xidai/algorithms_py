__author__ = 'Xidai'


class LinkedStack:

    class Node:
        def __init__(self):
            self.item = None
            self.next = None

    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first is None

    def push(self, item):
        new_node = self.Node()
        new_node.item = item
        new_node.next = self.first
        self.first = new_node

    def pop(self):
        old_node = self.first
        self.first = old_node.next
        return old_node.item

