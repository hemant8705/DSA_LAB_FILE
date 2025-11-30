# Experiment 04: Circular Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CSLL:
    def __init__(self):
        self.start = None

    def insert_begin(self, data):
        new = Node(data)
        if self.start is None:
            self.start = new
            new.next = self.start
            return
        temp = self.start
        while temp.next != self.start:
            temp = temp.next
        new.next = self.start
        temp.next = new
        self.start = new
