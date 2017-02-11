word = input('Enter your word: ')
element_dictionary = {}

def get_element():
    element_list = open('elements', 'r')
    for line in element_list:
        words = line.split('\t')
        element_name = words[0]
        element_symbol = words[1]
        element_dictionary[element_name] = element_symbol

def get_word(word):
	print(word)

def match_element():
    return;
get_element()
get_word(word)
print(element_dictionary)
