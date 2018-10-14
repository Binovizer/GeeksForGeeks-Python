from tree.node import Node
# from tree.traversals import in_order_traversal, post_order_traversal, pre_order_traversal, level_order_traversal
# from tree.height_of_tree import get_height
# from tree.count_leaves import get_leaves
# from tree.children_sum_property import is_sum_property
# from tree.mirror_tree import mirror
from tree.check_balanced_tree import is_balanced, is_balance_optimised

if __name__ == '__main__':
    tree = Node(7)
    left = Node(5)
    right = Node(2)
    tree.left = left
    tree.right = right
    leftleft = Node(2)
    left.left = leftleft
    leftright = Node(3)
    left.right = leftright
    rightleft = Node(2)
    right.left = rightleft
    rightright = Node(7)
    right.right = rightright
    leftleftleft = Node(2)
    left.left.left = leftleftleft
    # print("-------------In Order Traversal-------------")
    # in_order_traversal(tree)
    # print("\n-------------Post Order Traversal-------------")
    # post_order_traversal(tree)
    # print("\n-------------Pre Order Traversal-------------")
    # pre_order_traversal(tree)
    # print("\n-------------Level Order Traversal-------------")
    # level_order_traversal(tree)
    # print(get_height(tree))
    # print(get_leaves(tree))
    # print(is_sum_property(tree))
    # mirror(tree)
    # print("\n-------------Level Order Traversal-------------")
    # level_order_traversal(tree)
    # print(is_balanced(tree))
    print(is_balance_optimised(tree))


