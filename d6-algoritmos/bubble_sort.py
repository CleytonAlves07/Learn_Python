# Pior dos casos O(n²)
def bubble_sort(numbers: list):
    n = len(numbers)

    for ordered_elem in range(n - 1):
        for item in range(0, n - 1 - ordered_elem):
            if numbers[item] > numbers[item + 1]:
                # Troca com desacoplamento
                numbers[item], numbers[item +
                                       1] = numbers[item + 1], numbers[item]
    return numbers


numbers = [99, 9, 15, 55, 28, 64, 37, 48, 8, 83]
print(bubble_sort(numbers))
