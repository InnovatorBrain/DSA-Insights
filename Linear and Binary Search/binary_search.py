def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print(f"Target not found")


Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(Numbers, 10)
verify(result)
