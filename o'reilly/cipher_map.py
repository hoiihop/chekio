def recall_password(cipher_grille, ciphered_password):
    password = ''
    count = 4
    while count:
        trafaret_pos = [[a, b] for a, i in enumerate(cipher_grille) for b, j in enumerate(i) if j == 'X']
        password += ''.join(list(map(lambda x: ciphered_password[x[0]][x[1]], trafaret_pos)))
        cipher_grille = tuple(zip(*cipher_grille[::-1]))
        count -= 1 
    return password


if __name__ == '__main__':
    print(recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'