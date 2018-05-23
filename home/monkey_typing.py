def count_words(text: str, words: set) -> int:
    # res = []
    # text = text.lower()
    # for word in words:
    #     find_word = text.find(word.lower())
    #     if find_word != -1:
    #         res.append(find_word)
    # return len(res)
    return len([word for word in words if text.lower().find(word.lower()) != -1])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {
                       "how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {
                       "banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
