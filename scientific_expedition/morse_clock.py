def checkio(time_string: str) -> str:
    time_string_temp = ''
    for i in time_string.split(':'):
        if len(i) != 2:
            time_string_temp += ('0' + i)
        else:
            time_string_temp += i

    convert_time = ['{0:02b}'.format(int(time_string_temp[0])),
                    '{0:04b}'.format(int(time_string_temp[1])),
                    '{0:03b}'.format(int(time_string_temp[2])),
                    '{0:04b}'.format(int(time_string_temp[3])),
                    '{0:03b}'.format(int(time_string_temp[4])),
                    '{0:04b}'.format(int(time_string_temp[5]))]
    morse_time = []
    for i in convert_time:
        temp = ''
        for j in i:
            if j == '0':
                temp += '.'
            else:
                temp += '-'
        morse_time.append(temp)

    return '{} {} : {} {} : {} {}'.format(*morse_time)


if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
