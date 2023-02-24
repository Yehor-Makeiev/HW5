import re


def replace_spam_words(text, spam_words):
    for patern in spam_words:
        text = re.sub(patern, "*"*len(patern), text, flags=re.IGNORECASE ) 
    return print(text)

        

         
 
    
    
    


if __name__ == "__main__":
    replace_spam_words('Guido van Rossum began working on Python in the late 1980s, \
as a successor to the ABC programming PYTHOn language, and first \
released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python'])






