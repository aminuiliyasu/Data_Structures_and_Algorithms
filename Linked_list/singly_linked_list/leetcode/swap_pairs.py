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

    def swap_nodes_in_pairs(self):
        if self.length == 0 or self.length == 1:
            return None
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        current = self.head
        while current is not None and current.next is not None:
            next_node = current.next
            current.next = next_node.next
            next_node.next = current
            prev.next = next_node
            prev = current
            current = current.next
        self.head = dummy.next
        dummy = None
        



my_linked_list = LinkedList(1)
my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.print_list()

