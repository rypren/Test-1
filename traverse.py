
class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.name)

    __repr__ = __str__

def doStuff(info):
    print(info)

def traverse(node):
    if node is None:
        return
    # if node.left == None and node.right == None:
    #     doStuff(node)
    #     return
    else:
        doStuff(node)
        traverse(node.left)
        traverse(node.right)

n3 = Node("node-3")
n4 = Node("node-4")
n6 = Node("node-6")
n5 = Node("node-5", None, n6)
n1 = Node("node-1", n5)
n2 = Node("node-2", n3, n4)
n0 = Node("node-0", n1, n2)

traverse(n0)
