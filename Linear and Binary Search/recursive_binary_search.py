def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                """
                The recursion performed bellow by calling the function itself to check the target value
                This function should have a stoping condition
                The Number of time recursive function call itself called Recursive-Depth
                It takes O(log n) time
                """
                return recursive_binary_search(list[midpoint + 1 :], target)
            return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print(f"Target found: {result}")


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = recursive_binary_search(number, 15)
verify(result)
