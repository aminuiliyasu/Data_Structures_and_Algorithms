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
    def find_kth_node(self, k):
        if k <= 0 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow

my_linked_list = LinkedList(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(9)
my_linked_list.append(11)
my_linked_list.print_list()
print("Finding 3rd node from the end:")
print(my_linked_list.find_kth_node(3).value)