from node import Node
from operations import print_tree, add_node_by_path, edit_node, delete_node
from yaml_io import build_tree_from_yaml, write_tree_to_yaml


if __name__ == "__main__":

    # Manual tree demo (as shown in PDF sample
    print("Manual tree demo:")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print_tree(root)

    # Create a new tree
    root = Node(10)
    print("\nInitial tree:")
    print_tree(root)

    # 3. Add nodes to the tree
    print("\nAdding nodes:")
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    add_node_by_path(root, "LL", 3)
    add_node_by_path(root, "LR", 7)
    add_node_by_path(root, "RL", 12)
    add_node_by_path(root, "RR", 18)

    print("\nTree after additions:")
    print_tree(root)

    #  Edit a node value
    print("\nEditing node LR to value 100:")
    edit_node(root, "LR", 100)
    print_tree(root)

    #  Delete a node
    print("\nDeleting node RL:")
    delete_node(root, "RL")
    print_tree(root)

    # Build tree from YAML
    yaml_file = "test.yaml"
    print(f"\nBuilding tree from '{yaml_file}':")
    yaml_root = build_tree_from_yaml(yaml_file)

    print("\nTree built from YAML:")
    print_tree(yaml_root)

    print("\nWriting tree to output.yaml:")
    write_tree_to_yaml(root, "output.yaml")

