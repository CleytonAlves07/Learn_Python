def countdown(n):
    if n == 0:
        print("Fim!")
    else:
        print(n)
        countdown(n - 1)


# countdown(5)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# answer = factorial(10)
# print(answer)


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


# answer = sum(120)
# print(answer)

def count_even(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + count_even(n - 1)
    else:
        return count_even(n - 1)

# answer = count_even(275)
# print(answer)


def biggest_num_aux(list, size):
    if size == 1:
        return list[0]
    else:
        biggest = biggest_num_aux(list, size - 1)
        if biggest > list[size - 1]:
            return biggest
        else:
            return list[size - 1]


def biggest_num(list):
    size = len(list)
    return biggest_num_aux(list, size)


# print(biggest_num([1, 21, 300, 4, 57]))


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)
