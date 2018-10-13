from tree.traversals import in_order_traversal, post_order_traversal, pre_order_traversal, level_order_traversal
from tree.node import Node

if __name__ == '__main__':
    tree = Node(1)
    left = Node(2)
    right = Node(3)
    tree.left = left
    tree.right = right
    leftleft = Node(4)
    left.left = leftleft
    leftright = Node(5)
    left.right = leftright
    rightleft = Node(6)
    right.left = rightleft
    rightright = Node(7)
    right.right = rightright
    print("-------------In Order Traversal-------------")
    in_order_traversal(tree)
    print("\n-------------Post Order Traversal-------------")
    post_order_traversal(tree)
    print("\n-------------Pre Order Traversal-------------")
    pre_order_traversal(tree)
    print("\n-------------Level Order Traversal-------------")
    level_order_traversal(tree)



