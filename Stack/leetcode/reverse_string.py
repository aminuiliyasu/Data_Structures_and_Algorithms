class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.length = 1
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def peek(self):
        if self.length == 0:
            return None
        return self.top.value
    
    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.top
        if self.length == 1:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.next
            temp.next = None
        self.length -= 1
        return temp.value
    def reverse_string(self, s):
        stack = Stack(s[0])
        for i in range(1, len(s)):
            stack.push(s[i])
        result = ""
        for i in range(len(s)):
            result += stack.pop()
        return result

my_stack = Stack("h")
print(my_stack.reverse_string("hello"))