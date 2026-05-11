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

    def partition_list(self, x):
        if self.length == 0:
            return None
        D1 = Node(0)
        D2 = Node(0)
        prev1 = D1
        prev2 = D2
        temp = self.head
        while temp is not None:
            if temp.value < x:
                prev1.next = temp
                prev1 = prev1.next
            else:
                prev2.next = temp
                prev2 = prev2.next
            temp = temp.next
        prev1.next = D2.next
        prev2.next = None
        self.head = D1.next
        D2 = None
        D1 = None



my_linked_list = LinkedList(8)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.print_list()

print("After partitioning around 5:")
my_linked_list.partition_list(5)
my_linked_list.print_list()