def linear_search(list, target):
    """
    Returns the index position of target if it found, else return None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print(f"Target not found")


Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(Numbers, 9)
verify(result)
