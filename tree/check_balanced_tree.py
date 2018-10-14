from tree.height_of_tree import get_height


def is_balanced(tree):
    if tree is None:
        return True
    if abs(get_height(tree.left) - get_height(tree.right)) > 1:
        return False
    return is_balanced(tree.left) and is_balanced(tree.right)


class Height:
    def __init__(self, height=0):
        self.height = height


def is_balance_optimised(tree):
    height = Height()
    return is_balance_optimise_with_param(tree, height)


def is_balance_optimise_with_param(tree, height):
    left_height = Height()
    right_height = Height()
    if tree is None:
        return True
    left = is_balance_optimise_with_param(tree.left, left_height)
    right = is_balance_optimise_with_param(tree.right, right_height)
    height.height = max(left_height.height, right_height.height) + 1
    if abs(left_height.height - right_height.height) <= 1:
        return left and right
    return False
