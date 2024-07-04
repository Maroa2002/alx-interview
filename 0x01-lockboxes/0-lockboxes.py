#!/usr/bin/python3
""" Lockboxes """"


def canUnlockAll(boxes):
    """
        args:
            boxes: list of lists
        return: True or False
    """
    n = len(boxes)
    unlocked = [False] * n  # List to keep track of which boxes are unlocked
    unlocked[0] = True  # The first box is unlocked

    keys = [0]  # Start with the keys in the first box

    while keys:
        key = keys.pop(0)  # Get the next key
        # Iterate through all the keys in the current box
        for k in boxes[key]:
            # If the key opens a box that is not already unlocked
            if k < n and not unlocked[k]:
                unlocked[k] = True  # Mark the box as unlocked
                # Add the keys in the newly unlocked box to the keys list
                keys.append(k)
    # Return True if all boxes are unlocked, False otherwise
    return all(unlocked)
