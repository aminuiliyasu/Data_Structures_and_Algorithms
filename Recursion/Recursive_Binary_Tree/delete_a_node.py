class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_(self, current_node, value):
        if current_node is None:
            return None

        if value < current_node.value:
            current_node.left = self.__delete_(current_node.left, value)

        elif value > current_node.value:
            current_node.right = self.__delete_(current_node.right, value)

        else:
            # No children
            if current_node.left is None and current_node.right is None:
                return None

            # One child
            elif current_node.left is None:
                return current_node.right

            elif current_node.right is None:
                return current_node.left

            # Two children
            else:
                min_value = self.min_value(current_node.right)
                current_node.value = min_value
                current_node.right = self.__delete_(
                    current_node.right, min_value
                )

        return current_node

    def delete_node(self, value):
        self.root = self.__delete_(self.root, value)


my_tree = BinarySearchTree()

my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print('Delete 21:')
my_tree.delete_node(21)

print(my_tree.root.left.value)
print(my_tree.root.left.left.value)