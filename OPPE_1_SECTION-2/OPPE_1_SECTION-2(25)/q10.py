
n = int(input())
numbers = [int(input()) for _ in range(n)]
num_dic = {}
count = 0
for num in numbers:
    if num in num_dic:
        num_dic[num] += 1
    else:
        num_dic[num] = 1
max_values = max(num_dic.values())

result = []
for number in num_dic:
    if num_dic[number] == max_values:
        result.append(number)
result.sort()
print(result)
      