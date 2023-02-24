import re


def find_word(text, word):
    my_find = re.search(word, text)
    if my_find:
        my_dict = {
                "result": True,
                "first_index": my_find.span()[0],
                "last_index": my_find.span()[1],
                "search_string": word,
                "string": text
                    }
        return print(my_dict)
    else:
        my_dict = {
                "result": False,
                "first_index": None,
                "last_index": None,
                "search_string": word,
                "string": text
                    }
        return print(my_dict)
    
      
    
            













find_word("Guido van Rossum began working on Python in the late 1980s, \
          as a successor to the ABC programming language, and first released \
          it in 1991 as Python 0.9.0.", 'Python')