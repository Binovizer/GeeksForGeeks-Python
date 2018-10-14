def get_height(tree):
    if tree is None:
        return 0
    return max(get_height(tree.left), get_height(tree.right)) + 1
