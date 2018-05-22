import re
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    start = text.find(begin) 
    print(start)   
    finish = text.find(end)    
    start = (start + len(begin)) if start >= 0 else 0
    finish = finish if finish > 0 else len(text)

    print(start)    

    return text[start:finish]   


if __name__ == '__main__':
    print('Example:')    
    #print(between_markers('What is >apple<', '>', '<'))
    print(between_markers("Never send a human to do a machine's job.","Never","do"))
    

    # These "asserts" are used for self-checking and not for testing
    # assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    # assert between_markers("<head><title>My new site</title></head>",
    #                        "<title>", "</title>") == "My new site", "HTML"
    # assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    # assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    # assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    # assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    # print('Wow, you are doing pretty good. Time to check it!')