import csv

#TODO: Separate the code below to an interface!
class TraversalStrategy:
    def traverse(self, node):
        raise NotImplementedError("Traversal method should be implemented by subclasses.")

class DFSTraversal(TraversalStrategy):
    def traverse(self, node):
        elements = [node.content]
        for child in node.children:
            elements.extend(self.traverse(child))
        return elements


#TODO: Separate the code below to a class!
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

    def traverse(self, strategy):#TODO: Make sure, that strategy can always be taken by traverse and find a testing kit that allows putting types as restrictions to parameters of functions!
        """
        Traverses the tree using the specified method and returns a list of elements.
        """
        return self._dfs_traversal(self.root)#No typing is provided, strategy is a TraversalStrategy!
    def _dfs_traversal(self, node):
        """
        Perform depth-first search traversal.
        """
        elements = [node.content]
        for child in node.children:
            elements.extend(self._dfs_traversal(child))
        return elements
    
# Example CSV content
csv_content = """Name,Age,Occupation
Alice,30,Engineer
Bob,25,Designer"""


#TODO: Create a test instance from the code in the next period!
# Parse the CSV content into a tree
root_node = TreeNode.parse_csv_new(csv_content)
tree_doc = TreeDocument(root_node)

# Create a DFS traversal strategy
dfs_strategy = DFSTraversal()

# Perform DFS traversal
elements_dfs = tree_doc.traverse(dfs_strategy)

# Print the elements in DFS order
print("DFS Traversal Result:")
for element in elements_dfs:
    print(element)

#TODO: Separate the code below to a test file!
import pytest
# Test data
test_data = [
    (
        """Name,Age,Occupation\nAlice,30,Engineer\nBob,25,Designer""",
        ["CSV Root", "Header", "Alice | 30 | Engineer", "Bob | 25 | Designer"]
    ),
    # Add more test cases here
]

@pytest.mark.parametrize("csv_content,expected", test_data)
def test_dfs_traversal(csv_content, expected):
    root_node = TreeNode.parse_csv_new(csv_content)
    tree_doc = TreeDocument(root_node)
    dfs_strategy = DFSTraversal()
    result = tree_doc.traverse(dfs_strategy)
    assert result == expected