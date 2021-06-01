def list_of_n_random_elements():
    from random import randint
    n = int(input('Сечас создам список из n элементов\nВведите n -> '))
    lst = [randint(0, 1000) for i in range(n)]
    return lst


a = list_of_n_random_elements()
print(a)