import yaml
from node import Node


def build_tree_from_dict(data):
    if data is None:
        return None

    node = Node(data.get("value"))
    node.left = build_tree_from_dict(data.get("left"))
    node.right = build_tree_from_dict(data.get("right"))

    return node


def build_tree_from_yaml(filename):
    with open(filename, "r") as file:
        data = yaml.safe_load(file)

    return build_tree_from_dict(data)


def tree_to_dict(node):
    if node is None:
        return None

    return {
        "value": node.value,
        "left": tree_to_dict(node.left),
        "right": tree_to_dict(node.right)
    }


def write_tree_to_yaml(root, filename):
    with open(filename, "w") as file:
        yaml.dump(tree_to_dict(root), file)
