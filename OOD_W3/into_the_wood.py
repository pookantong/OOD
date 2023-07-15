class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
class IntoTheWoods:
    
    def __init__(self):
        self.stack = Stack()

    def aState(self, new_height):
        while not self.stack.isEmpty() and self.stack.peek() <= new_height:
            self.stack.pop()
        self.stack.push(new_height) 
        
    def bState(self):
        return len(self.stack.items)

    def start(self, inp):
        for input in inp:
            act = input.split()
            act_state = act[0]
            if act_state == 'A':
                self.aState(int(act[1]))
            else:
                print(self.bState())
                

woods = IntoTheWoods()
inp = input('Enter Input : ').split(',')
woods.start(inp)

