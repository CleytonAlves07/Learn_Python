
# Pior caso O(n²), melhor caso O(n)
def insertion_sort(numbers: list):
    n = len(numbers)

    for index in range(1, n):
        key = numbers[index]
        new_position = index - 1

        while new_position >= 0 and numbers[new_position] > key:
            numbers[new_position + 1] = numbers[new_position]
            new_position = new_position - 1

        numbers[new_position + 1] = key
    return numbers


numbers = [99, 9, 15, 55, 28, 64, 37, 48, 8, 83]
# print(insertion_sort(numbers))

# sorted() O(n log n)

print(sorted(numbers))
