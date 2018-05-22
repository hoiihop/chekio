def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    if text[0].islower():
        text = text[0].upper() + text[1:]
        
    if not text.endswith('.'):
        text = text + '.'
    return text


if __name__ == '__main__':
    print("Example:")   

    print(correct_sentence("greetings, friends"))
    print(correct_sentence("Greetings, friends"))
    print(correct_sentence("Greetings, friends."))
    print(correct_sentence("hi"))
    # These "asserts" are used for self-checking and not for an auto-testing
    # assert correct_sentence("greetings, friends") == "Greetings, friends."
    # assert correct_sentence("Greetings, friends") == "Greetings, friends."
    # assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    # assert correct_sentence("hi") == "Hi."
    # print("Coding complete? Click 'Check' to earn cool rewards!")