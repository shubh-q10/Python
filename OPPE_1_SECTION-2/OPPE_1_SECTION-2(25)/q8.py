s = input().split(" ")
vowels = "aeiouAEIOU"
v_count = 0
result_list = []

for word in s:
    for i in word:
        if i in vowels:
            v_count += 1
    result_list.append(f"{word}({v_count})")

    v_count = 0
print(" ".join(result_list))            
     