from collections import deque
def tree_by_levels(node):
    if node is None:
        return []
    visited = []
    que = deque([node])
    
    while que:
        cur = que.popleft()
        visited.append(cur.value)
        if cur.left is not None:
            que.append(cur.left)
        if cur.right is not None:
            que.append(cur.right)
    return visited
