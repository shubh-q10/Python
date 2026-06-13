'''
Deinterleave Even and Odd Indices in String
Write a function deinterleave that takes a string s as input and returns a new string where the characters at even indices are placed before the characters at odd indices.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Examples

"abcdef" -> "acebdf"
"12345" -> "13524"
'''

s = "abcdef" 
def deinterleave(s: str) -> str:
    even_c = s[::2]
    odd_c = s[1::2]
    print(even_c+odd_c)
            

    
deinterleave(s)


