# Write a function in python that can reverse a string using stack data structure.
from stack import Stack
input_str="We will conquere COVID-19"
stk=Stack()
def reverse_string(input_str:str)->str:
    rtn_str=""
    for char in input_str:
        stk.push(char)

    while not stk.is_empty():
        rtn_str+=stk.pop()

    return rtn_str

print(reverse_string(input_str))


