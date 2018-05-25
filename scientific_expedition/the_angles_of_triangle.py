from typing import List
import math

def checkio(a: int, b: int, c: int) -> List[int]:
    if a < (b + c) and b < (a + c) and c < (a + b):
        alpha = round(math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c))))
        beta = round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c))))
        gamma = 180 - (alpha + beta)
        
        return sorted([alpha, beta, gamma])
    else:
        return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")