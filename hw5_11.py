import re


def find_all_words(text, word):
    # my_list = []
    my_find = re.findall(word, text, re.IGNORECASE)
    return print(my_find)
    # if my_find:
    #     my_list.append(word)
    # return print(my_find)    





find_all_words('Guido van Rossum began working on Python in the late 1980s, \
               as a successor to the ABC programming PYTHOn language, and first \
               released pYthoN it in 1991 as Python 0.9.0. pythOn ', 'Python')