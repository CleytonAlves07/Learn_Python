from math import floor
"""Dado um array verifique se ele se repete mais de 2 vezes.

[1, 2, 2, 6, 6, 6, 7, 10]

Para o elemento ser repetido mais de 2 vezes 
ele precisa ser maior que 25%

[1, 2, 2, {6}, 6, {6}, 7, 10]

Checando o elemento na posição 3 e 25% depois se eles 
se repetirem a condição foi atendida

É necessário utilizar apenas 
75% de array, já que ele não vai atender ao que foi pedido 
e pode gerar um indexError 

[1, 2, 2, 6, 6, 6, {7}, 10], {}

"""

# Condição mais performática


def repeat_number(array):
    twenty_five_percent = floor(len(array)//4)
    seventy_five_percent = len(array) - twenty_five_percent

    for index, element in enumerate(array[:seventy_five_percent]):
        if element == array[index + twenty_five_percent]:
            return print('element: ', element)

    return -1


# repeat_number([1, 2, 2, 3, 6, 6, 6, 7, 10])
# repeat_number([1, 2, 2, 3, 6, 6, 7, 7, 7, 9, 10])
# repeat_number([1, 2, 2, 3, 6, 6, 7, 7, 9, 10])


# O(n²) - Função não performática

def repeat_number_bad_function(array):
    for element in array:
        count = 0
        tag = floor(len(array)//4)
        for element2 in array:
            if element == element2:
                count += 1
            if count > tag:
                return print('element: ', element)

    return -1


repeat_number_bad_function([1, 2, 2, 3, 6, 6, 7, 7, 9, 10])
