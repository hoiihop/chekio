# Давайте посмотрим на сортировку. Дан массив с особыми правилами.
# Массив (tuple) содержит различные числа. Вам необходимо отсортировать их, но отсортировать на основе абсолютных значений в возрастающем порядке. Для примера, последовательность (-20, -5, 10, 15) будет отсортирована следующим образом (-5, 10, 15, -20). Ваша функция должна возвращать список (list) или кортеж (tuple).
# Входные данные: Массив чисел как кортеж (tuple).
# Выходные данные: Список (list) или кортеж (tuple) (но не генератор) отсортированный по абсолютным значениям чисел.
# Дополнение: Результат вашей функции вы увидите как список (list) в панели выводов результатов проверки.
# Предусловия: len(set(abs(x) for x in array)) == len(array)
# 0 < len(array) < 100
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)

def checkio(numbers_array: tuple) -> list:
    temp = list(numbers_array)
    temp.sort(key=lambda x: abs(x))
    return temp

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")