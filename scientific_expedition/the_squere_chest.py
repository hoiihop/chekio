from typing import List

def checkio(lines_list: List[List[int]]) -> int:    
    count = 0
    for item in lines_list:
        start_x, start_y = item        
        x = start_x
        y = start_y
        while True:
            print([x, y])
            if [x, y] in lines_list:
                x = y
                y += 1                
            elif [x, y] in lines_list:
                x = y
                y += 4
            elif [x, y] in lines_list:
                x = y - 1
                y = y
            elif [x, y] in lines_list:
                x = y - 4
                y = y
            if start_x == x and start_y == y:
                count += 1
                break
    return count    


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2], [1, 5], [2, 6], [5, 6]]))
    # print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
    #                [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
    #                [10, 14], [12, 16], [14, 15], [15, 16]]))

    # assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
    #                  [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
    #                  [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    # assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
    #                  [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
    #                  [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    # assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    # assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    # assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
    #                  [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    # print("Coding complete? Click 'Check' to earn cool rewards!")