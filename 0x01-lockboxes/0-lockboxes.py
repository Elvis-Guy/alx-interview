def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    keys = [0]  # Start with the key to the first box
    unlocked = [False] * n
    unlocked[0] = True

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
