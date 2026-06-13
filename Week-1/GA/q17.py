'''
Recall operator precedence

parenthesis > not > and > or


not (a or b) and c

first look inside parenthesis a or b then not(a or b) that is true only if both a,b are false 
so, not(a or b) is equivalent to (not a) and (not b)
full expression is (not(a) and not(b)) and c or (not(a or b) and c) which is last option


'''