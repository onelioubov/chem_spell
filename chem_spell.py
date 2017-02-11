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
def match_element(iter_word,out_string):
    iter_word = list(iter_word)
    element_string = ""
    while iter_word:
        letter = iter_word[0].upper()
        if len(iter_word) > 1 and letter in element_dictionary and letter + iter_word[1] in element_dictionary: 
            if element_weights[letter] > element_weights[letter + iter_word[1]]:
                out_string += letter
                element_string += element_dictionary[letter] + ", "
                iter_word.pop(0)
            else:
                out_string += letter + iter_word[1]
                element_string += element_dictionary[letter + iter_word[1]] + ", "
                iter_word.pop(0)
                iter_word.pop(0)
        elif letter in element_dictionary:
            out_string += letter
            element_string += element_dictionary[letter] + ", "
            iter_word.pop(0)
        elif len(iter_word) > 1 and letter + iter_word[1] in element_dictionary:
            out_string += letter + iter_word[1]
            element_string += element_dictionary[letter + iter_word[1]] + ", "
            iter_word.pop(0)
            iter_word.pop(0)
        else:
            iter_word.pop(0)
            out_string += "?"
    print (out_string + " (" + element_string.lower().rstrip(', ') + ")")

#gets input word and calls the element matching function
def get_word():
    word = input('Enter your word or type "exit" to quit: ')
    while word not in ['exit']:
        out_string = ""
        match_element(word,out_string)
        word = input('Enter your word or type "exit" to quit: ')

get_element()
get_word()
