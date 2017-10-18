"""Algorithm to create a new book based on The Communist Manifesto."""

# Workers of the World: Unite! 

import random

def create_source_dict(path):

    source_text = open(path).read().replace('\n', '')
    source_text.split()

    source_dict = {}

    for word in source_text:
        word_group = source_dict.setdefault(word, [])
        word_group.append(source_text[word + 1])
        word_group.append(source_text[word + 2])

    return source_dict

def find_search_key(path):
    book_dict = create_source_dict(path)
    

def main(num, path):
    book_dict = create_source_dict(path)
    search_key = "string"
    # call function to get first 2 words here
    generated_text = ''
    for reps in range(num):
        added_text = book_dict[search_key][random.randint(0, len(book_dict[search_key]))]
        generated_text += added_text
        search_key = added_text
    return generated_text



