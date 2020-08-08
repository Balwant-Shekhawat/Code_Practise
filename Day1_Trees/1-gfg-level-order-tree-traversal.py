# URL : https://www.geeksforgeeks.org/level-order-tree-traversal/
# Level Order Traversal/BFS is done using Queue
# Time Complexity = O(n) where n is number of nodes in the binary tree
# Space Complexity = O(n) where n is number of nodes in the binary tree

def levelOrder(head):
    if head is None:
        return None
    queue = []
    queue.append(head)
    output = []
    while len(queue):
        popedItem = queue.pop(0)
        output.append(popedItem.data)

        if popedItem.left is not None:
            queue.append(popedItem.left)

        if popedItem.right is not None:
            queue.append(popedItem.right)
    
    return output
        
