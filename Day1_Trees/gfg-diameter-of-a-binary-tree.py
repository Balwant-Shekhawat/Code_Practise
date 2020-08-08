# URL : https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
# Diameter is the longest path between two nodes in a tree, in simpler way,
# Diameter is max of (leftHeight+rightHeigt+1) among all nodes

# Space Complexity : O(N) as we used recursion call stack
# Time Complexity : O(N)

maxDiameter = 1

def height(node):
    global maxDiameter 
    if node is None:
        return 0

    leftHeight = height(node.left)
    rightHeight = height(node.right)
    maxDiameter = max(maxDiameter, (leftHeight+rightHeight+1))
    return  max( leftHeight, rightHeight) + 1
        
def diameter(root):
    global maxDiameter
    maxDiameter = 1
    

    height(root)
    return maxDiameter
        

# class Tree:
#     def __init__(self, node):
#         self.root = node
#         self.left = None
#         self.right = None

# def main():
#     n = Tree(1)
#     n.left = Tree(2)
#     n.right = Tree(3)
#     n.left.left = Tree(4)
#     n.left.right = Tree(5)
#     n.left.right.left = Tree(6)
#     n.right.right = Tree(7)
#     n.right.right.right = Tree(8)
#     n.right.right.right.right = Tree(9)
#     n.right.right.right.right.right = Tree(10)
#     n.right.right.right.right.left = Tree(11)
#     n.right.right.right.right.left.right = Tree(12)

#     # h = height(n)
#     # print("Height", h)
#     d = diameter(n)
#     print("Diameter", d)

# main()
