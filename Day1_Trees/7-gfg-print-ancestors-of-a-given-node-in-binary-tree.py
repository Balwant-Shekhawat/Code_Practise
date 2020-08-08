output = []
def printAncestors(root, target):
    global output 
    if root is None:
        return None

    if root.data == target:
        return output
    else:
        output.append(root.data)

    printAncestors(root.left, target)
    printAncestors(root.right, target)
