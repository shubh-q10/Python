words = ["hello", 'world', 'school', 'open', 'baby', 'beautiful']

def length_analysis(words):
    D = {}
    for word in words:
        D[word] = len(word)
    return D

print(length_analysis(words))