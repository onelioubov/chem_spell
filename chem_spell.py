word = input('Enter your word: ')
element_dictionary = {}
element_weights = {}

#takes a tab-delimeted elements table and adds it to a dictionary
def get_element():
    element_list = open('elements', 'r')
    for line in element_list:
        words = line.split('\t')
        element_dictionary[words[1]] = words[0]
        stripped = words[3].lstrip('(').rstrip(')')     #some atomic weights are listed as averages, denoted by parentheses; this strips them off
        element_weights[words[1]] = stripped
    return element_dictionary,element_weights

#matches elements to word segments
def match_element(iter_word,new_string):
    iter_word = list(iter_word)
    element_string = ""
    while iter_word:
        letter = iter_word[0].upper()
        if len(iter_word) > 1 and letter in element_dictionary and letter + iter_word[1] in element_dictionary: 
            if element_weights[letter] > element_weights[letter + iter_word[1]]:
                new_string += letter
                element_string += element_dictionary[letter] + " "
                iter_word.pop(0)
            else:
                new_string += letter
                new_string += iter_word[1]
                element_string += element_dictionary[letter + iter_word[1]] + " "
                iter_word.pop(0)
                iter_word.pop(0)
        elif letter in element_dictionary:
            new_string += letter
            element_string += element_dictionary[letter] + " "
            iter_word.pop(0)
        elif len(iter_word) > 1 and letter + iter_word[1] in element_dictionary:
            new_string += letter
            new_string += iter_word[1]
            element_string += element_dictionary[letter + iter_word[1]] + " "
            iter_word.pop(0)
            iter_word.pop(0)
        else:
            iter_word.pop(0)
            new_string += "?"
    print (new_string + " ( " + element_string + ")")

def get_word(word):
    new_string = ""
    match_element(word,new_string)
    return new_string

get_element()
get_word(word)
