# Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).
# Входные данные: Положительное целое число.
# Выходные данные: Произведение цифр как целочисленное (int).
# Предусловия: 0 < number < 106

def checkio(number: int) -> int:
    res = 1
    for i in str(number):
        i = int(i)
        if i != 0:
            res *= i

    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")