import sys
class Node:
    def__init__(self,key):
        self.data=key
        self.next=none
class StackLinkedList:
    def__init__(self):
        self.root=none
    def isEmpty(self):
        if(self.root is None):
            return True
        return False
    def push(self,key):
        node=Node(key)
        node.next=self.root
        self.root=node
        print("The element is pushed and top points to => ", self.root.data)
    def pop(self):
        deletedElement = -sys.maxsize-1
        if(self.isEmpty()):
            print("Stack Underflow")
        else:
            topElement=self.root.data
            self.root=self.root.next
        return topElement
    def peek(self):
        topElement= -sys.maxsize-1
        if (self.isEmpty()):
            print("Stack Underflow")
        else:
            topElement=self.data.root
        return topElement
    

 

