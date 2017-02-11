word = input('Enter your word: ')
element_dictionary = {}
def get_element():
    element_list = open('elements', 'r')
    for line in element_list:
        words = line.split('\t')
        element_dictionary[words[1]] = words[0]
    return element_dictionary

def match_element(iter_word,new_string):
    iter_word = list(iter_word)
    while iter_word:
        letter = iter_word[0].upper()
        if letter in element_dictionary:
            new_string += letter
            iter_word.pop(0)
        elif len(iter_word) > 1 and letter + iter_word[1] in element_dictionary:
            new_string += letter
            new_string += iter_word[1]
            iter_word.pop(0)
            iter_word.pop(0)
        else:
            iter_word.pop()
            new_string += "?"
    print (new_string)

def get_word(word):
    new_string = ""
    match_element(word,new_string)
    return new_string

get_element()
get_word(word)
#print(final)
