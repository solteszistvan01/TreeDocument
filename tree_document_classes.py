import csv


class TreeNode:

    def __init__(self, content):

        self.content = content

        self.children = []

        self.parent = None



    def add_child(self, child_node):

        self.children.append(child_node)

        child_node.parent = self



    def is_root(self):

        return self.parent is None



    def __str__(self, level=0, last_child=True):

        """

        Create a string representation of the node and its children, visually similar to the `tree` command.

        """

        prefix = "    " * (level - 1) + ("|__ " if last_child else "|-- ")

        parts = [prefix + self.content] if level > 0 else [self.content]

        for i, child in enumerate(self.children):

            parts.append(child.__str__(level + 1, i == len(self.children) - 1))

        return "\n".join(parts)
    


    @staticmethod
    def parse_csv(csv_content):
        """
        Parses CSV content and returns the root node of the tree.
        """
        root = TreeNode("CSV Root")
        reader = csv.reader(csv_content.splitlines())

        header = next(reader)
        for column in header:
            column_node = TreeNode(column)
            root.add_child(column_node)

        for row in reader:
            for i, cell in enumerate(row):
                cell_node = TreeNode(cell)
                root.children[i].add_child(cell_node)

        return root

    @staticmethod
    def parse_csv_new(csv_content):
        """
        Parses CSV content into a tree where each row becomes a token under the root.
        """
        root = TreeNode("CSV Root")
        header_node = TreeNode("Header")
        root.add_child(header_node)
        reader = csv.reader(csv_content.splitlines())

        next(reader)

        for row in reader:
            row_data = " | ".join(row)
            row_node = TreeNode(row_data)
            header_node.add_child(row_node)

        return root


# Define the TreeDocument class

class TreeDocument:

    def __init__(self, root_node):

        self.root = root_node



    def __str__(self):

        return self.root.__str__()