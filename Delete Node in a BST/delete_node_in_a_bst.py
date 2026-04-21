# class Node:
#     def __init__(self, left, right, data):
#         self.val = data
#         self.right = right
#         self.left = left

from collections import deque

class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return None
        if root.val == key:
            pass
        probe = root
        prev_probe = None
        found = True
        is_right = None
        while True:
            if key > probe.val:
                if not probe.right:
                    found = False
                    break
                prev_probe = probe
                probe = probe.right
                is_right = True
            elif key < probe.val:
                if not probe.left:
                    found = False
                    break
                prev_probe = probe
                probe = probe.left
                is_right = False
            else:
                break
        if not found:
            return root
        if probe.left and probe.right:
            parent = probe
            succ = probe.right
            while succ.left:
                parent = succ
                succ = succ.left
            probe.val = succ.val
            if parent.left == succ:
                parent.left = succ.right
            else:
                parent.right = succ.right
        elif probe.right or probe.left:
            nx = probe.right or probe.left
            if prev_probe:
                if is_right:
                    prev_probe.right = nx
                else:
                    prev_probe.left = nx
            else:
                return nx
        else:
            if prev_probe:
                if is_right:
                    prev_probe.right = None
                else:
                    prev_probe.left = None
            else:
                return None
        return root
