# Pre-order traversal
def pre_order(node, visited=None):
    if visited is None:
        visited = []
    if node is not None:
        visited.append(node.data)
    else:
        return []
    if node.left is not None:
        visited = pre_order(node.left, visited)
    if node.right is not None:
        visited = pre_order(node.right, visited)
    return visited

# In-order traversal
def in_order(node, visited=None):
    if visited is None:
        visited = []
    if node is None:
        return []
    if node.left is not None:
        visited = in_order(node.left, visited)
    visited.append(node.data)
    if node.right is not None:
        visited = in_order(node.right, visited)
    return visited

# Post-order traversal
def post_order(node, visited=None):
    if visited is None:
        visited = []
    if node is None:
        return []
    if node.left is not None:
        visited = post_order(node.left, visited)
    if node.right is not None:
        visited = post_order(node.right, visited)
    visited.append(node.data)
    return visited

