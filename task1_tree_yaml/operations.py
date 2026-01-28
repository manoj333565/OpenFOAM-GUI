from node import Node


def print_tree(root, level=0, label="Root"):
    if root is None:
        return

    print("    " * level + f"{label}:{root.value}")
    print_tree(root.left, level + 1, "L")
    print_tree(root.right, level + 1, "R")


def add_node_by_path(root, path, value):
    current = root

    for direction in path[:-1]:
        if direction == 'L':
            if current.left is None:
                current.left = Node(None)
            current = current.left

        elif direction == 'R':
            if current.right is None:
                current.right = Node(None)
            current = current.right

    if path[-1] == 'L':
        current.left = Node(value)
    elif path[-1] == 'R':
        current.right = Node(value)

def edit_node(root, path, new_value):
    current = root

    for direction in path:
        if direction == 'L':
            current = current.left
        elif direction == 'R':
            current = current.right

        if current is None:
            print("Invalid path. Cannot edit.")
            return

    current.value = new_value


def delete_node(root, path):
    if not path:
        return root

    current = root

    for direction in path[:-1]:
        if direction == 'L':
            current = current.left
        elif direction == 'R':
            current = current.right

        if current is None:
            print("Invalid path. Cannot delete.")
            return root

    if path[-1] == 'L':
        current.left = None
    elif path[-1] == 'R':
        current.right = None

    return root


