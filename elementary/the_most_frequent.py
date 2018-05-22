# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
# Input: a list of strings.
# Output: a string.

def most_frequent(data: list) -> str:
    count = 0
    res = ''
    for i in data:
        cnt = data.count(i)
        if cnt > count:
            count = cnt
            res = i

    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
    
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')