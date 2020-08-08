def getSize(node):
    if node is None:
        return 0

    return getSize(node.left) + getSize(node.right) + 1