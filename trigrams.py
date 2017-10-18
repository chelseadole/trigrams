"""Algorithm to create a new book based on The Communist Manifesto."""

# Workers of the World: Unite! 

def create_source_dict(path):

    source_text = open(path).read().replace('\n', '')
    source_text.split()

    source_dict = {}

    for word in source_text:
        word_group = source_dict.setdefault(word, [])
        word_group.append(source_text[word + 1])
        word_group.append(source_text[word + 2])

    return source_dict

def main(num, path):
    



