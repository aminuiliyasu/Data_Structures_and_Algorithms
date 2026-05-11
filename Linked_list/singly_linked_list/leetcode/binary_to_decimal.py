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

    def binary_to_decimal(self):
        if self.length == 0:
            return None
        temp = self.head
        decimal_value = 0
        power = self.length - 1
        while temp is not None:
            decimal_value += temp.value * (2 ** power)
            power -= 1
            temp = temp.next
        return decimal_value



my_linked_list = LinkedList(1)
my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.print_list()

print("Binary to Decimal:")
print(my_linked_list.binary_to_decimal())