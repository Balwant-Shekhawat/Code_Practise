def printKDistant(root,k):
    if root is None:
        return None

    if k == 0:
        print(root.data)

    printKDistant(root.left, k-1)
    printKDistant(root.right, k-1)