def last_word_starts_with_upper_case(sentence: str):
    words = sentence.split()
    last_upper_word = None
    for word in words:
        if word and word[0].isupper():
            last_upper_word = word
            
        else:
            return None
    return last_upper_word

print(last_word_starts_with_upper_case("This is a Test sentence"))
print(last_word_starts_with_upper_case("no upper word here"))
    
    
   
   
   
   
   #Given a sentence, find the last word that starts with an uppercase letter. 
   # If no such word exists, return None. Words in the sentence are separated by spaces. 
   # Assume no punctuations will be present.