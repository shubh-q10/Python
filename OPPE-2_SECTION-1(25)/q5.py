'''
Surround First Two and Last Two with Square Brackets


Given a string s, you need to surround the first two and the last two characters of the string with square brackets [].

Assueme the string s will have at least 4 characters.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Example

"hello" -> "[he]l[lo]"
"python" -> "[py]th[on]"
"brackets" -> "[br]acke[ts]"
"four" -> "[fo][ur]"

'''
s = "hello"
def surround_first_two_and_last_two_with_brackets(s: str):
    first = s[0:2]
    mid = s[2:-2]
    last = s[-2:]
    return (f"[{first}]{mid}[{last}]")

print(surround_first_two_and_last_two_with_brackets(s))
