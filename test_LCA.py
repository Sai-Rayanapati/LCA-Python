from LCA import Node, LCA


class TestLCA:
    def testLCA(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        # Nodes with same parent node
        assert LCA.LCA(4, 5, root) is 2

        # Nodes with different parent nodes
        assert LCA.LCA(4, 6, root) is 1

        # Nodes with different depths
        assert LCA.LCA(3, 4, root) is 1

        # Nodes as parent and child
        assert LCA.LCA(2, 4, root) is 2

        # Same Nodes
        assert LCA.LCA(1, 1, root) is 1

        # Nodes not present
        assert LCA.LCA(2, 8, root) is -1
