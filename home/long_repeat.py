def long_repeat(line):
    if line:
        if line.count(line[0]) != len(line):
            res = []
            temp = line[0]
            count = 1
            for char in line[1:]:                                    
                if char != temp:
                    res.append(count)
                    temp = char
                    count = 1                
                else:
                    count += 1                        
            return max(res)
        else:
            return len(line)
    else:
        return 0


if __name__ == '__main__':
    #print(long_repeat('sdsffffse'))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('abababa') == 1, "Good"
    print('"Run" is good. How is "Check"?')
