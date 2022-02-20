class StackArray:
    max=5

    stack=[]

    def __init__(self):
        self.top=-1

    def isEmpty(self):
        if(self.top==0):
            return True
        return False
    
    def isFull(self):
        if (self.top>=self.max-1):
            return True
        return False
    
    def push (self,key):
        if(self.isFull()):
            print("Overflow")
            return False
        self.top+=1
        self.stack.append(key)
        print("The element is pushed and top points to => ",self.stack[self.top])
        return True
    def pop(self):
        if(self.isEmpty()):
            print("Stack Underflow")
            return -1
        deletedElement = self.stack[self.top]
        self.top -= 1
        return deletedElement

    def peek(self):
        if(self.isEmpty()):
            print("There is no record in the stack.")
            return -1

        peekElement = self.stack[self.top]
        return peekElement
if __name__ == '__main__': 
    s = StackArray()
    s.push(30)
    s.push(40)
    s.push(50)
    s.push(60)
    s.push(70)