def get_words_after_the(sentence: str) -> list:
    words = sentence.split()
    wordlist = []
    for  i in  range(len(words) - 1):
        if words[i] == "The" or words[i] == "the":
            wordlist.append(words[i + 1])
    return wordlist
            
            
            
print(get_words_after_the("The sun is the main the source"))


            
