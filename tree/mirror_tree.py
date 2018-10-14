def mirror(tree):
    if tree is None:
        return
    if tree.left is None and tree.right is None:
        return
    mirror(tree.left)
    mirror(tree.right)
    tree.left, tree.right = tree.right, tree.left
