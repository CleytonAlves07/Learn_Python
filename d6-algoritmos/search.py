
def binary_search(numbers: list, target: int):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            return mid
        if target < numbers[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


numbers = [2, 3, 5, 6, 7, 8, 9, 12, 23, 37, 37, 46, 63, 73, 74, 97]
element = binary_search(numbers, 2)
print(f'Element found in {element} position')
