from caeser_cipher.corpus_loader import word_list, name_list
import re

def count_words(text):
     # return count of words found in corpus
    words_to_test = text.split()
    word_count = 0
    for test_word in words_to_test:
        word = re.sub(r'[^A-Za-z]+','', test_word)
        if word.lower() in word_list or word in name_list:
            word_count += 1
        else:
            pass
    return word_count
