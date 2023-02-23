# def is_spam_words(text:str, spam_words:str, space_around=False):
#     first_audit = " " + spam_words  
#     second_audit = spam_words + " "
#     third_audit = spam_words + "."

#     if text.lower().find(spam_words.lower()) != -1:
#         space_around = False 
    
#     if text.lower().startswith(spam_words.lower()) or text.lower().find(first_audit) != -1:
#         space_around = True 
    
#     if text.lower().find(second_audit.lower()) != -1:
#        space_around = True 

#     if text.lower().find(third_audit.lower()) != -1:
#         space_around = True 
#     return  True
    





def is_spam_words(text:str, spam_words:str, space_around=False):
    spam_words = spam_words.lower()
    text = text.lower()
    flagg1 = False
    text1 = ' ' + spam_words
    if space_around == False:
        if text.startswith(spam_words) or text.find(text1) != -1:
            flagg1 = True
    else:
         if text.find(spam_words) != -1:
            flagg1 = True
    return flagg1   
    




if __name__ == "__main__":
    is_spam_words("Moloh", "lOh")