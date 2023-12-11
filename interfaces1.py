class TraversalStrategy:
    def traverse(self, node):
        raise NotImplementedError("Traversal method should be implemented by subclasses.")

class DFSTraversal(TraversalStrategy):
    def traverse(self, node):
        elements = [node.content]
        for child in node.children:
            elements.extend(self.traverse(child))
        return elements
