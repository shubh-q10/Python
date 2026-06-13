n = int(input())
vowels = "aeiou"
for _ in range(n):
    line = input()
    changed_line = ""
    for char in line:
        if char.lower() in vowels:
            changed_line += char.upper()
        else:
            changed_line += char.lower()
            
    print(changed_line)
