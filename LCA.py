
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LCA(n1, n2, root):
    if nodePresent(root, n1) is not True or nodePresent(root, n2) is not True:
        return -1

    else:
        return findLCA(root, n1, n2)


def findLCA(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root.data

    left = findLCA(root.left, n1, n2)
    right = findLCA(root.right, n1, n2)

    if left and right:
        return root.data

    return left if left is not None else right


def nodePresent(root, num):
    if root is None:
        return False

    if root.data is num:
        return True

    if root.left is not None and nodePresent(root.left, num):
        return True

    if root.right is not None and nodePresent(root.right, num):
        return True

    else:
        return False

