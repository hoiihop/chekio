def best_stock(data):
    # res = list(data.values())
    # res.sort()
    # res.reverse()

    # for key, value in data.items():
    #     if value == res[0]:
    #         return key
    return max(data, key=data.get)


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")