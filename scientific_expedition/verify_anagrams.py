def verify_anagrams(first_word, second_word):
    first_word = list(''.join(first_word.lower().split()))
    second_word = list(''.join(second_word.lower().split()))
    if len(first_word) == len(second_word):
        for letter in second_word:
            if letter in first_word:
                first_word.remove(letter)
            else:
                return False
    else:
        return False
    
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"