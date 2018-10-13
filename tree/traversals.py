from tree.node import Node
from queue import Queue


def in_order_traversal(tree):
    if tree is not None and isinstance(tree, Node):
        in_order_traversal(tree.left)
        print(tree.data, end=' ')
        in_order_traversal(tree.right)


def pre_order_traversal(tree):
    if tree is not None and isinstance(tree, Node):
        print(tree.data, end=' ')
        pre_order_traversal(tree.left)
        pre_order_traversal(tree.right)


def post_order_traversal(tree):
    if tree is not None and isinstance(tree, Node):
        post_order_traversal(tree.left)
        post_order_traversal(tree.right)
        print(tree.data, end=' ')


def level_order_traversal(tree):
    if tree is not None:
        print(tree.data, end=' ')
        q = Queue()
        q.put(tree)
        while not q.empty():
            head = q.get()
            if head is not None:
                if head.left is not None:
                    print(head.left.data, end=' ')
                    q.put(head.left)
                if head.right is not None:
                    print(head.right.data, end=' ')
                    q.put(head.right)
