word_string = 'abcd'
word_list = ['a', 'b', 'c', 'd']
word_tupple = ('a', 'b', 'c', 'd')

word_list[0] = 'z'
print(word_list)

word_string[0] = 'z'  # doesnot support item assignment
print(word_string)

word_tupple[0] = 'z'  # doesnot support item assignment
print(word_tupple)

