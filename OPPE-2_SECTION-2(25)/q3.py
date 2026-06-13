'''

Given a string s, count the number of vowels and consonants that appear at even indices in the string (0-based indexing). Ignore non-alphabetical characters.

Implement the function count_vowels_and_consonants_in_even_indices that returns the counts as described above.

The string s can have both upper and lower case letters.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Examples

"abcdeaeiou" -> (4, 1)
Characters at even indices are: 'a', 'c', 'e', 'e', 'u'.
Vowels: 'a', 'e', 'e', 'u' (4 vowels).
Consonants: 'c' (1 consonant).
"a11bc11de11" -> (2, 1)
Characters at even indices are: 'a', '1', 'b', '1', 'd', '1'.
Vowels: 'a' (1 vowel).
Consonants: 'b', 'd' (2 consonants).
"ABCDE" -> (2, 1)
Characters at even indices are: 'A', 'C', 'E'.
Vowels: 'A', 'E' (2 vowels).
Consonants: 'C' (1 consonant).


'''

#I HAVE USED ENUMERATE COZ INDEX() SHOW THE INDEX OF FIRST OCCURRENCE OF THE CHAR IN STRING



s = "abcdeaeiou" 

def count_vowels_and_consonants_in_even_indices(s: str) -> tuple:
    vowels = 0
    consonants = 0
    for i, x in enumerate(s):
        if x.isalpha() and i % 2 == 0:
            if x in "aeiouAEIOU":
                vowels += 1
            else:
                consonants += 1                
            
            
            
    return (vowels, consonants)

print(count_vowels_and_consonants_in_even_indices(s))
    
