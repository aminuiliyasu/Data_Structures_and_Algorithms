class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self,current_node,value):
        if current_node==None:
            return Node(value)
        if value<current_node.value:
            current_node.left=self.__r_insert(current_node.left,value)
        if value>current_node.value:
            current_node.right=self.__r_insert(current_node.right,value)
        return current_node
    def r_insert(self,value):
        if self.root==None:
            self.root=Node(value)
        return self.__r_insert(self.root,value)
my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)    
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.root.left.left.value)
print(my_tree.root.left.right.value)
print(my_tree.root.right.left.value)
print(my_tree.root.right.right.value)
