"""Algorithm to create a new book based on The Communist Manifesto."""

# Workers of the World: Unite! 

import random

def create_source_dict(path):

    source_text = open(path).read().replace('\n', ' ')
    source_text = source_text.split(' ')

    coupled_source = iter(source_text)
    next(coupled_source)
    coupled_output = [' '.join((first_word, second_word))
        for first_word, second_word in zip(source_text, coupled_source)]

    source_dict = {}

    for word in range(len(coupled_output)):
        try: 
            word_group = source_dict.setdefault(coupled_output[word], [])
            word_group.append(source_text[word + 2])
        except IndexError: 
            word_group = source_dict.setdefault(coupled_output[word], [])
    return source_dict

def find_search_key(path, book_dict):
    first_key = random.choice(list(book_dict))
    return first_key

def main(num, path):
    book_dict = create_source_dict(path)
    search_key = find_search_key(path, book_dict)
    generated_text = ''
    for reps in range(num):
        added_text = book_dict[search_key][random.randint(0, len(book_dict[search_key]) - 1)]
        generated_text += added_text + ' '
        search_key = search_key.split(' ')[1] + ' ' + added_text
    return generated_text



