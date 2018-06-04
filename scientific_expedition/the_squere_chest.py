from typing import List


def checkio(lines_list: List[List[int]]) -> int:
    temp_lines_list = [sorted(i) for i in lines_list]
    temp_lines_list.sort()
    count = 0

    for item in temp_lines_list:
        if (item[1] - item[0]) == 1:
            for i in range(3):                
                squere_list = []
                squere_list.append(item)
                if i == 0:
                    x, y = squere_list[-1]
                    squere_list.append([x + 1, y + 4])
                    squere_list.append([x + 4, y + 4])
                    squere_list.append([x, x + 4])
                else:
                    for j in range(i):
                        x, y = squere_list[-1]
                        squere_list.append([x + 1, y + 1])

                    for j in range(i + 1):
                        x, y = squere_list[-1]
                        squere_list.append([y, y + 4])

                    x, y = squere_list[-1]
                    squere_list.append([y - 1, y])
                    for j in range(i):
                        x, y = squere_list[-1]                                               
                        squere_list.append([x - 1, x])

                    for j in range(i + 1):
                        x, y = squere_list[-1]
                        squere_list.append([x - 4, x])

                temp = []
                for i in squere_list:
                    if i in temp_lines_list:
                        temp.append(i)

                if len(temp) == len(squere_list):
                    count += 1
                
    return count


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 5], [5, 9], [9, 13], [13, 14], [2, 3], [4, 8], [6, 7], [6, 10], [
          7, 11], [1, 2], [14, 15], [16, 15], [16, 12], [8, 12], [8, 4], [10, 11], [3, 7]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]])
            == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10],
                     [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    print("Coding complete? Click 'Check' to earn cool rewards!")
