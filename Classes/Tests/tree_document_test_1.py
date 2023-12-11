import pytest
from your_module import TreeNode, TreeDocument, DFSTraversal  # Import your classes

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