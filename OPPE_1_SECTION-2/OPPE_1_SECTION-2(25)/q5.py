def last_word_starts_with_upper_case(sentence: str):
    words = sentence.split(" ")
    last = None
    for word in words:
        if word and word[0].isupper():
            last = word
    return last
            
print(last_word_starts_with_upper_case("THis is the thing which is Big enough to have "))