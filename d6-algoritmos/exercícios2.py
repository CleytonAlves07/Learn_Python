import time
# Solução para diminuir a complexidade de uma
# função quando é
# necessário percorrer um array.
# Considerando que a lista está ordenada

# Solução mais performática!


def check_sum(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer < right_pointer:
        test_sum = numbers[left_pointer] + numbers[right_pointer]
        if test_sum == target:
            return True
        if test_sum < target:
            left_pointer += 1
        else:
            right_pointer -= 1

    return False


def test_check_sum():
    assert check_sum([4, 5, 6, 7, 8, 10, 12, 15, 28, 30], 15) is True
    assert check_sum([4, 5, 6, 7, 8, 10, 12, 15, 28, 30], 95) is False

    assert check_sum([10, 20, 30, 40, 50, 60, 70, 80, 90], 90) is True
    assert check_sum([10, 20, 30, 40, 50, 60, 70, 80, 90], 190) is False

# O(n²)


def check_sum_quad(numbers, target):
    for index, num in enumerate(numbers):
        for num2 in numbers[index + 1:]:
            if num + num2 == target:
                return True
    return False


def test_check_sum_quad():
    assert check_sum_quad([4, 5, 6, 7, 8, 10, 12, 15, 28, 30], 15) is True
    assert check_sum_quad([4, 5, 6, 7, 8, 10, 12, 15, 28, 30], 95) is False

    assert check_sum_quad([10, 20, 30, 40, 50, 60, 70, 80, 90], 90) is True
    assert check_sum_quad([10, 20, 30, 40, 50, 60, 70, 80, 90], 190) is False


if __name__ == "__main__":
    five_thousand = list(range(0, 5000))
    ten_thousand = list(range(0, 10000))
    twenty_thousand = list(range(0, 20000))

    print('\n')
    start_time = time.time()
    check_sum(five_thousand, 9900)
    print(f"Função check_sum -> 5 mil: {(time.time() - start_time)} segundos")

    print('\n')
    start_time = time.time()
    check_sum(ten_thousand, 99000)
    print(f"Função check_sum -> 10 mil: {(time.time() - start_time)} segundos")

    print('\n')
    start_time = time.time()
    check_sum(twenty_thousand, 99000)
    print(f"Função check_sum -> 20 mil: {(time.time() - start_time)} segundos")

    print('\n')
    start_time = time.time()
    check_sum_quad(five_thousand, 9900)
    print(
        f"Função check_sum_squad -> 5 mil: {(time.time() - start_time)} segundos")

    print('\n')
    start_time = time.time()
    check_sum_quad(ten_thousand, 99000)
    print(
        f"Função check_sum_squad -> 10 mil: {(time.time() - start_time)} segundos")

    print('\n')
    start_time = time.time()
    check_sum_quad(twenty_thousand, 99000)
    print(
        f"Função check_sum_squad -> 20 mil: {(time.time() - start_time)} segundos")
