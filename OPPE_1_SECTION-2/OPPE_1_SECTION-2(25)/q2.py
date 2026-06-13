n = int(input())
vowels = "aeiou"
for _ in range(n):
    line = input()
    converted_line = ""
    for char in line:
        if char.lower() in vowels:
            converted_line += char.upper()
        else:
            converted_line += char.lower()
    print(converted_line)