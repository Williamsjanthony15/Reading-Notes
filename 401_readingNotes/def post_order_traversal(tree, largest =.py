def post_order_traversal(tree, largest = 0):
    if tree.root is None:
        return largest
    if tree.root.left is not None:
        if tree.left.value > largest:
            largest = tree.left.value
        post_order_traversal(tree.left, largest)
    if tree.root.right is not None:
        if tree.right.value > largest:
            largest = tree.right.value
        post_order_traversal(tree.right, largest)

    post_order_traversal(tree)