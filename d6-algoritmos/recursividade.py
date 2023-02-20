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


answer = factorial(5)
print(answer)
