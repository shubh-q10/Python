sum = 0
n = input()
while n != "-1":
    sum = int(n) + int(n[::-1])
    n = input()
    if str(sum) == str(sum)[::-1]:
        print(n)