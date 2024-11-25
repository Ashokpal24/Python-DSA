import collections
class Stack:
    def __init__(self):
        self.container=collections.deque()

    def pop(self)->int:
        if not self.is_empty():
            return self.container.pop()
        return None
    
    def push(self,value)->None:
        self.container.append(value)
    
    def peek(self)->int:
        if not self.is_empty():
            return self.container[-1]
        return None
    
    def is_empty(self)->bool:
        return len(self.container)==0

# stk=Stack()
# stk.push(1)
# stk.push(2)
# stk.push(3)
# print("stack empty:",stk.is_empty())
# print("Current top:",stk.peek())
# print("Value popped:",stk.pop())
# print("Value popped:",stk.pop())
# print("Value popped:",stk.pop())
# print("Value popped:",stk.pop())
# print("Current top:",stk.peek())
# print("stack empty:",stk.is_empty())


