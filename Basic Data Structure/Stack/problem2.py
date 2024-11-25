# Write a function in python that checks if paranthesis in the string are balanced or not. 
# Possible parantheses are "{}',"()" or "[]"
from stack import Stack

brackets={
    "[":"]","{":"}","(":")"
}
def is_balanced(input_str:str)->bool:
    stk=Stack()
    for char in input_str:
        if char in brackets.keys():
            stk.push(char)
        elif char in brackets.values():
            if char==brackets.get(stk.peek(),None):
                stk.pop()
            else:
                stk.push(char)
    return stk.is_empty()

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

        
    
