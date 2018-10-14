def get_leaves(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    return get_leaves(tree.left) + get_leaves(tree.right)
