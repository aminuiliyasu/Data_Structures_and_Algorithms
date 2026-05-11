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

    def decimal_to_binary(self):
        if self.length == 0:
            return None
        temp = self.head
        decimal_value = 0
        power = self.length - 1
        while temp is not None:
            decimal_value += temp.value * (10 ** power)
            power -= 1
            temp = temp.next
        binary_string = ""
        if decimal_value == 0:
            return "0"
        while decimal_value > 0:
            binary_string = str(decimal_value % 2) + binary_string
            decimal_value //= 2
        return binary_string
        



my_linked_list = LinkedList(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.print_list()

print("Decimal to Binary:")
print(my_linked_list.decimal_to_binary())