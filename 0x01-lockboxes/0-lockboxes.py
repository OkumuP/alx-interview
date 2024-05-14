#!/usr/bin/python3
"""
Lock boxes solution
"""

def canUnlockAll(boxes):
    # Set to track visited boxes
    visited = set()

    # Queue for BFS traversal
    queue = deque([0])

    # Mark the first box as visited
    visited.add(0)

    # BFS traversal
    while queue:
        current_box = queue.popleft()

        # Check all keys in the current box
        for key in boxes[current_box]:
            # If the key opens a box we haven't visited yet, visit it
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)

    # If we visited all boxes, return True, otherwise return False
    return len(visited) == len(boxes)
