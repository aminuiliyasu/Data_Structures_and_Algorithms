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
    
    def remove_duplicates(self):
        if self.length == 0:
            return None
        current = self.head
        checker = current.next
        my_set = set([current.value])
        while checker is not None:
            if  checker.value in my_set:
                current.next = checker.next
                self.length -= 1
            else:
                my_set.add(checker.value)
                current = checker
            checker = checker.next



my_linked_list = LinkedList(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(6)
my_linked_list.append(11)
my_linked_list.print_list()
print("After removing duplicates:")
my_linked_list.remove_duplicates()
my_linked_list.print_list()