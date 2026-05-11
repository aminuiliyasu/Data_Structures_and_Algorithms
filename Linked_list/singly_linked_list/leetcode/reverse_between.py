class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def reverse_between(self, start_index, end_index):
        if self.length == 0 or start_index >= end_index or start_index < 0 or end_index >= self.length:
            return 
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for _ in range(start_index):
            prev = prev.next
        current = prev.next
        for _ in range(end_index - start_index):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        self.head = dummy.next
        dummy = None

        


my_linked_list = LinkedList(8)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.print_list()

print("After reversing between index 2 and 4:")
my_linked_list.reverse_between(2, 4)
my_linked_list.print_list()
