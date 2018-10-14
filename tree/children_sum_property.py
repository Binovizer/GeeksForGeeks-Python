def is_sum_property(tree):
    if tree is None:
        return 1
    elif tree.left is None and tree.right is None:
        return 1
    elif tree.left is not None and tree.right is None:
        if tree.left.data == tree.data:
            return is_sum_property(tree.left);
        else:
            return 0
    elif tree.right is not None and tree.left is None:
        if tree.right.data == tree.data:
            return is_sum_property(tree.right)
        else:
            return 0
    elif tree.left.data + tree.right.data == tree.data:
        return is_sum_property(tree.left) and is_sum_property(tree.right)
    else:
        return 0

