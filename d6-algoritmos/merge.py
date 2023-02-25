
# Função O(n log n)
def merge_sort(items: list):
    # Caso base
    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


def merge(left: list, right: list):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left == []:
        result += right
    else:
        result += left

    return result


numbers = [99, 9, 15, 55, 28, 64, 37, 48, 8, 83]
print(merge_sort(numbers))
