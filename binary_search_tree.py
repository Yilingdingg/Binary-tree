class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def Insert(root_value, new_value):
    if root_value==None:
        return Node(new_value)
    if root_value.value < new_value:
        root_value.right=Insert(root_value.right, new_value)
    else:
        root_value.left=Insert(root_value.left, new_value)
    
tree=None

for i in range (5):
    value=int(input("Enter values you want to add:"))
    tree=Insert(tree,value)